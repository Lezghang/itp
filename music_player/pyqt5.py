import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QSlider, 
                            QLabel, QFileDialog, QListWidget, QHBoxLayout, 
                            QVBoxLayout, QWidget, QStyle, QAction, QMenu)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QPixmap

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音乐播放器")
        self.setGeometry(100, 100, 800, 600)
        
        # 媒体播放器和播放列表
        self.playlist = QMediaPlaylist()
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        
        # 创建UI组件
        self.init_ui()
        
        # 连接信号和槽
        self.connect_signals()
        
        # 初始化主题
        self.dark_mode = False
        self.apply_theme()

    def init_ui(self):
        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 菜单栏
        menubar = self.menuBar()
        file_menu = menubar.addMenu('文件')
        
        open_file_action = QAction('打开文件', self)
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)
        
        open_folder_action = QAction('打开文件夹', self)
        open_folder_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_folder_action)
        
        theme_action = QAction('切换主题', self)
        theme_action.triggered.connect(self.toggle_theme)
        menubar.addAction(theme_action)
        
        # 播放列表
        playlist_label = QLabel("播放列表")
        self.playlist_widget = QListWidget()
        main_layout.addWidget(playlist_label)
        main_layout.addWidget(self.playlist_widget)
        
        # 专辑封面
        self.album_art = QLabel()
        self.album_art.setAlignment(Qt.AlignCenter)
        self.album_art.setMinimumHeight(200)
        self.album_art.setText("No Album Art")
        main_layout.addWidget(self.album_art)
        
        # 当前播放信息
        self.song_info = QLabel("未播放任何歌曲")
        self.song_info.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.song_info)
        
        # 进度条
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 0)
        self.position_slider.sliderMoved.connect(self.set_position)
        main_layout.addWidget(self.position_slider)
        
        # 时间标签
        time_layout = QHBoxLayout()
        self.current_time = QLabel("00:00")
        self.total_time = QLabel("00:00")
        time_layout.addWidget(self.current_time)
        time_layout.addStretch()
        time_layout.addWidget(self.total_time)
        main_layout.addLayout(time_layout)
        
        # 控制按钮
        control_layout = QHBoxLayout()
        
        self.prev_button = QPushButton()
        self.prev_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.prev_button.clicked.connect(self.playlist.previous)
        
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_pause)
        
        self.next_button = QPushButton()
        self.next_button.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.next_button.clicked.connect(self.playlist.next)
        
        self.stop_button = QPushButton()
        self.stop_button.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stop_button.clicked.connect(self.player.stop)
        
        self.shuffle_button = QPushButton()
        self.shuffle_button.setIcon(self.style().standardIcon(QStyle.SP_BrowserReload))
        self.shuffle_button.clicked.connect(self.toggle_shuffle)
        
        # 音量控制
        volume_layout = QHBoxLayout()
        volume_label = QLabel("音量:")
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(70)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.player.setVolume(70)
        
        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)
        
        # 添加按钮到控制布局
        control_layout.addWidget(self.prev_button)
        control_layout.addWidget(self.play_button)
        control_layout.addWidget(self.next_button)
        control_layout.addWidget(self.stop_button)
        control_layout.addWidget(self.shuffle_button)
        control_layout.addLayout(volume_layout)
        
        main_layout.addLayout(control_layout)
        
        # 状态栏
        self.statusBar().showMessage("就绪")

    def connect_signals(self):
        # 播放器信号
        self.player.stateChanged.connect(self.update_play_button)
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)
        self.player.currentMediaChanged.connect(self.update_song_info)
        
        # 播放列表信号
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        
        # 播放列表控件信号
        self.playlist_widget.doubleClicked.connect(self.playlist_double_clicked)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "音频文件 (*.mp3 *.wav *.ogg)")
        if file_name:
            self.add_to_playlist(file_name)

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "打开文件夹")
        if folder:
            for file_name in os.listdir(folder):
                if file_name.endswith(('.mp3', '.wav', '.ogg')):
                    self.add_to_playlist(os.path.join(folder, file_name))

    def add_to_playlist(self, file_path):
        url = QUrl.fromLocalFile(file_path)
        self.playlist.addMedia(QMediaContent(url))
        file_name = os.path.basename(file_path)
        self.playlist_widget.addItem(file_name)
        
        # 如果这是添加的第一首歌，开始播放
        if self.playlist.mediaCount() == 1:
            self.playlist.setCurrentIndex(0)
            self.player.play()

    def play_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def toggle_shuffle(self):
        if self.playlist.playbackMode() == QMediaPlaylist.Random:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
            self.statusBar().showMessage("顺序播放")
        else:
            self.playlist.setPlaybackMode(QMediaPlaylist.Random)
            self.statusBar().showMessage("随机播放")

    def set_volume(self, value):
        self.player.setVolume(value)

    def set_position(self, position):
        self.player.setPosition(position)

    def update_play_button(self, state):
        if state == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def update_position(self, position):
        self.position_slider.setValue(position)
        
        # 更新当前时间显示
        minutes = position // 60000
        seconds = (position % 60000) // 1000
        self.current_time.setText(f"{minutes:02d}:{seconds:02d}")

    def update_duration(self, duration):
        self.position_slider.setRange(0, duration)
        
        # 更新总时间显示
        minutes = duration // 60000
        seconds = (duration % 60000) // 1000
        self.total_time.setText(f"{minutes:02d}:{seconds:02d}")

    def update_song_info(self, media_content):
        if media_content.isNull():
            self.song_info.setText("未播放任何歌曲")
            self.album_art.setText("No Album Art")
            return
            
        file_path = media_content.canonicalUrl().toLocalFile()
        file_name = os.path.basename(file_path)
        self.song_info.setText(f"正在播放: {file_name}")
        
        # 这里可以添加读取专辑封面的代码
        # 简化版本，使用默认封面
        self.album_art.setText("No Album Art")

    def playlist_position_changed(self, position):
        self.playlist_widget.setCurrentRow(position)

    def playlist_double_clicked(self, index):
        self.playlist.setCurrentIndex(index.row())
        self.player.play()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("""
                QMainWindow { background-color: #2E3440; color: #E5E9F0; }
                QListWidget { background-color: #3B4252; color: #E5E9F0; }
                QLabel { color: #E5E9F0; }
                QSlider::groove:horizontal { background: #4C566A; }
                QSlider::handle:horizontal { background: #88C0D0; }
                QPushButton { background-color: #434C5E; color: #E5E9F0; border: 1px solid #4C566A; }
                QPushButton:hover { background-color: #5E81AC; }
                QMenuBar { background-color: #2E3440; color: #E5E9F0; }
                QMenuBar::item:selected { background-color: #434C5E; }
                QMenu { background-color: #3B4252; color: #E5E9F0; }
                QMenu::item:selected { background-color: #434C5E; }
            """)
            self.statusBar().showMessage("暗色主题已启用")
        else:
            self.setStyleSheet("")  # 恢复默认主题
            self.statusBar().showMessage("亮色主题已启用")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())