#!/bin/bash

# Preview CSV file
ls

# Apply SQL query to Spotify_MusicAttributes.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" Spotify_MusicAttributes.csv

# Reformat the output using csvlook 
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv | csvlook

# Re-direct output to new file: ShortestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > ShortestSong.csv
    
# Preview newly created file 
csvlook ShortestSong.csv