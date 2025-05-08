# PyQt5 Music Player

## Introduction

This is a desktop music player application developed using Python and the PyQt5 library. The player provides a user-friendly interface for playing music files, managing playlists, and adjusting audio settings. It supports basic playback controls, volume adjustment, progress tracking, and playlist management. The application also features a theme toggle between light and dark modes for improved user experience.

## Features

- **Playback Controls**: Play, pause, stop, skip to next or previous tracks
- **Volume Control**: Adjust volume with a slider
- **Progress Tracking**: View and control playback progress with a timeline
- **Playlist Management**: Add individual files or entire folders to the playlist
- **Metadata Display**: Shows the current playing track information
- **Theme Switching**: Toggle between light and dark themes
- **Shuffle Playback**: Randomize playlist order
- **User-Friendly Interface**: Clean and intuitive design

## Installation

To run this application, you need to have Python 3 installed along with the PyQt5 library. Follow these steps to get started:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/)
2. **Install PyQt5**: Open your terminal or command prompt and run:
   ```
   pip install PyQt5
   ```
3. **Download the Source Code**: Clone this repository or download the source files
4. **Run the Application**: Navigate to the directory containing the source code and run:
   ```
   python music_player.py
   ```

## Usage

1. **Opening Files**: Use the "File" menu to open individual music files or entire folders
2. **Playing Music**: Double-click on a track in the playlist to start playing
3. **Playback Controls**: Use the buttons at the bottom to control playback
4. **Volume Adjustment**: Use the volume slider on the right side
5. **Progress Control**: Drag the progress bar to change the current position in the track
6. **Theme Toggle**: Click the "Toggle Theme" option in the menu bar to switch between light and dark modes
7. **Shuffle Playback**: Click the shuffle button to randomize the playlist order

## Development Process

### Initial Setup

The project began with setting up the basic PyQt5 application structure. The main window was created with a central widget and layout management. The initial challenge was understanding how PyQt5's layout system works, especially with nested layouts. This was resolved by studying the official PyQt5 documentation and experimenting with different layout configurations.

### Core Functionality

Implementing the media player functionality involved working with PyQt5's `QMediaPlayer` and `QMediaPlaylist` classes. Key challenges included:

1. **Audio Playback**: Getting the audio to play required understanding how to properly set up the media player and playlist. This involved creating a playlist, adding media content, and managing the playback state.
2. **Metadata Extraction**: Displaying song information such as title and artist proved challenging as the initial implementation only showed the file name. This was addressed by planning to integrate the `mutagen` library in future updates to properly extract metadata from audio files.
3. **Playlist Management**: Managing the playlist both in terms of the GUI representation and the underlying `QMediaPlaylist` required careful synchronization between the two. This was achieved by connecting signals and slots to update the UI when the playlist changes.

### UI Development

Creating an intuitive and visually appealing interface involved:

1. **Layout Design**: Organizing widgets in a logical and aesthetically pleasing manner. This required multiple iterations to find the right balance between functionality and visual appeal.
2. **Theme Implementation**: Implementing the theme toggle involved understanding how to apply stylesheets dynamically in PyQt5. The solution involved creating two different stylesheets and switching between them based on user preference.
3. **Responsive Design**: Ensuring the interface looks good on different screen sizes. This was managed by using appropriate layout managers and setting minimum and preferred sizes for widgets.

### Debugging and Optimization

Common issues encountered during development included:

1. **Null Media Content**: When switching tracks, there were instances where the media content was null, causing errors. This was resolved by checking for null media content before attempting to access its properties.
2. **Timeline Synchronization**: The progress bar and time labels not updating correctly. This was fixed by properly connecting the `positionChanged` and `durationChanged` signals from the media player.
3. **Style Application**: Stylesheets not applying correctly to all widgets. This was addressed by ensuring stylesheets were applied consistently and understanding how PyQt5's style inheritance works.

## Future Improvements

While the current version provides basic music player functionality, there are several areas for future improvement:

1. **Album Art Display**: Implement proper album art extraction and display using libraries like `mutagen`
2. **Enhanced Metadata**: Show more detailed song information such as album and track number
3. **Keyboard Shortcuts**: Add support for keyboard controls
4. **Playback Modes**: Add repeat options (repeat one, repeat all)
5. **Equalizer**: Implement audio equalizer for sound customization
6. **Search Functionality**: Add search within the playlist
7. **Playlist Saving/Loading**: Allow users to save and load playlists

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- PyQt5 Documentation: For providing detailed information on the library's functionality
- Qt Framework: For the multimedia classes used in this project
- Python Community: For the wealth of resources and tutorials available online
