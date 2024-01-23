# Backend and OBS

This is a little project about

This little project is a test I did for a job to deploy videos from a server to the streamer's obs. The idea was to implement custom ads that the user uploads, from the server.

Apart from the videos, you can also access to real time APIS and images (from an api or from your own server) thanks to an OBS plugin [Click here](https://obsproject.com/forum/resources/url-api-source-live-data-media-and-ai-on-obs-made-simple.1756/).

## How it works
In order to use this program you will need to download all the necessary dependencies and obs. The only thing you have to do is to launch the server and go to the video part, upload a video and copy its address. In OBS in any scene, go to sources -> browser -> give it a name -> put the copied url and configure it.

The videos are changed automatically every time you upload a new file and update. You can only upload one file at a time as the obs only reads one address.

Keep in mind that this is a very improvable version as it is only a test and I use this repo as memory.

Thank you very much and if you want to contribute, perfect!
