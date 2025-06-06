# Adding an AirPlay button to your Safari media controls

**Framework**: Webkitjs

Create a custom control that adds AirPlay to your Safari media player. 

#### Overview

Although default controls are available for audio and video elements in your Safari webpage, you can also create your own custom media controls. One of the custom controls you should add is an AirPlay button.

##### 2940017

In this example, the custom controls for a video have only a Play button and a hidden Pause button: 

```other
<video id="video" src="my-video.mp4"></video>
<div id="controls">
    <button id="playButton">Play</button>
    <button id="pauseButton" hidden>Pause</button>
</div>
```

##### 2940019

Add markup for the AirPlay button, setting it to hidden by default to mimic the behavior of the AirPlay button in default controls. The default button appears only when AirPlay is available.

```other
<video id="video" src="my-video.mp4"></video>
<div id="controls">
    <button id="playButton">Play</button>
    <button id="pauseButton" hidden>Pause</button>
    <button id="airPlayButton" hidden disabled>AirPlay</button>
</div> 
```

##### 2940021

To show the AirPlay button when AirPlay is available, you add an event listener for the `webkitplaybacktargetavailabilitychanged` event. This event detects when AirPlay availability changes, and it changes the visibility of the AirPlay button from the above default markup. 

> **Note**: To conserve battery power, listen for this event only for as long as needed, and then stop listening. If the button is not visible, controls are hidden, or the user is in fullscreen mode, stop listening. 

To conserve battery power, listen for this event only for as long as needed, and then stop listening. If the button is not visible, controls are hidden, or the user is in fullscreen mode, stop listening. 

```javascript
if (window.WebKitPlaybackTargetAvailabilityEvent) {
    video.addEventListener('webkitplaybacktargetavailabilitychanged',
        function(event) {
            switch (event.availability) {
            case "available":
                airPlayButton.hidden = false;
                airPlayButton.disabled = false;
                break;
            case "not-available":
                airPlayButton.hidden = true;
                airPlayButton.disabled = true;
                break;
        } }); 
} 
```

##### 2940025

Add this block of code to use the native AirPlay route picker in your controls. With this route picker, you can add and select an available AirPlay device:

```javascript
if (!window.WebKitPlaybackTargetAvailabilityEvent)
    return;
var airPlayButton = document.getElementById("airPlayButton");
var video = document.getElementById("video");
airPlayButton.addEventListener('click', function(event) {
    video.webkitShowPlaybackTargetPicker();
});
```

##### 2940027

Use the code below to listen for the event `webkitcurrentplaybacktargetiswirelesschanged`. This event fires when a media element starts or stops AirPlay playback. Use this event to update styles.

```javascript
 if (!window.WebKitPlaybackTargetAvailabilityEvent)
     return;
 var video = document.getElementById("video");
 video.addEventListener('webkitcurrentplaybacktargetiswirelesschanged', 
     function(event) {
         updateAirPlayButtonWirelessStyle();
         updatePageDimmerForWirelessPlayback();
     });
```

## See Also

- [Adding Picture in Picture to your Safari media controls](adding_picture_in_picture_to_your_safari_media_controls.md)
  Create a custom control that adds Picture in Picture to your Safari media player. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/adding_an_airplay_button_to_your_safari_media_controls)*