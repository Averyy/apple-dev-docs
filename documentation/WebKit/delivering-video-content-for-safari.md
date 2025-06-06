# Delivering Video Content for Safari

**Framework**: Webkit

Improve the performance and appearance of video in your website in Safari.

#### Overview

When adding video content to your website you have several playback and optimization options which can help to improve the playback controls and performance of video for the user:

- For video streaming, use HTTP Live Streaming. See [`HTTP Live Streaming`](https://developer.apple.com/documentation/HTTP-Live-Streaming).
- For static video files, use H.264-encoded MP4 files.
- For more customization and control over the loading process, use Media Source Extensions (MSE). See [`Advanced Media for the Web`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2014/504/).

To deliver video content in your website:

1. Add your video to your website so it can play. Determine whether to autoplay the video or trigger playback with a user interaction.
2. Optimize your video playback by making use of low-power mode or by using a short video file in an image element instead of animated GIFs.
3. Add the appropriate playback controls for inline, full screen, or WebRTC, depending on the type of content in the video.

##### Play a Video in Your Webpage

Using `<video>` elements in HTML5 markup allows you to embed video on your website.

Safari honors the `preload="metadata"` attribute, allowing `<video>` and `<audio>` elements to load enough media data to determine that media’s size, duration, and available tracks. A `<video>` element can use the `play()` method to automatically play without user gestures only when it contains no audio tracks or has its `muted` property set to `true`. If this video element gains an audio track or becomes unmuted without a user gesture,  playback pauses. Playback stops if the video element isn’t visible onscreen or is out of the viewport.

###### Enable Video Autoplay

Video elements that include `<video autoplay>` play automatically when the video loads in Safari on macOS and iOS, only if those elements also include the  `playsinline` attribute. For more information on inline playback, see [`Enable Inline Video Playback`](delivering-video-content-for-safari#Enable-Inline-Video-Playback.md).

By default, autoplay executes only if the video doesn’t contain an audio track, or if the video element includes the `muted` attribute. Video playback pauses if the element gains an audio track, becomes unmuted without user interaction, or if the video is no longer onscreen (either by CSS or due to the user scrolling the page). The video doesn’t pause unless the user clicks or taps the video. This same expectation applies to WebRTC one-way video conferencing. For more information on WebRTC playback controls, see [`Add WebRTC Playback Controls`](delivering-video-content-for-safari#Add-WebRTC-Playback-Controls.md).

Autoplay video when the user expects it to autoplay in your website. For example, autoplay video in interfaces where video playback is the purpose of the webpage, like a video-sharing or hosting website.

##### Optimize Video Content for Safari

To ensure that video content takes advantage of the hardware and software optimizations of your machine and Safari, get your video into low-power mode and use MP4 files instead of animated GIFs.

###### Reduce Power Usage in Video Playback

On certain macOS devices, such as the Retina MacBook or MacBook Pro, hardware configurations make video elements play in low-power mode. This mode allows your video to render efficiently to the display without an expensive color processing step.

Low-power mode is available for a video element that is in full screen, against a black background, and is the only content onscreen. Having only the video element onscreen means a full-screen video layout. In other cases, the system needs to convert the video to RGB so it composites correctly with other content onscreen.

Set the CSS property `display:none` for all non-video elements on your webpage while the video is playing, to ensure that low-power mode is enabled for your video element. Then, check that the remaining background behind the video is black.

###### Use Quartz Debug to Test Low Power Regions

To ensure that low-power mode is working correctly, test the efficiency of your web content using the Show Detached Regions feature of Quartz Debug.

First, test on your machine’s built-in or primary monitor, and ensure that your MacBook or MacBook Pro is not using external monitors.

Then, open the Quartz Debug app. Quartz Debug is part of the Graphics Tools package for Xcode, available from the Mac Developer Portal. In Quartz Debug, choose Tools > Show Detached Regions.

![Enable Show Detached Regions in the Quartz Debug Tools menu.](https://docs-assets.developer.apple.com/published/c67a5f5a5242d14fde82a4b15043e21c/media-3030255%402x.png)

This tool places a color overlay on the desktop. Red represents normal power usage (where everything is composited), and no overlay represents low-power usage for video. If the full-screen video display is using low-power mode, the red color overlay disappears.

![A red overlay appears over video content that is not using low-power mode.](https://docs-assets.developer.apple.com/published/fafe099846375284211076ba22a3ed0e/media-3030260%402x.png)

> **Note**:  Use Web Inspector to adjust CSS properties in the browser to see which changes enable low-power mode. Check to see if there are sub-layers attached to the displayed element that contains your video. If there are, adjust your stylesheets with these changes so that there are no sub-layers, then low-power mode can take effect.

 Use Web Inspector to adjust CSS properties in the browser to see which changes enable low-power mode. Check to see if there are sub-layers attached to the displayed element that contains your video. If there are, adjust your stylesheets with these changes so that there are no sub-layers, then low-power mode can take effect.

If you use `<video controls>`, then in full screen your video will get low-power mode automatically when the controls disappear. If you make your own custom media controls, then make sure everything is hidden when the user is watching the video. Avoid having items such as timelines remain after it’s clear the user is just watching the video. For more information on debugging low-power mode and other media issues, see [`Debugging Media in Web Inspector`](https://developer.apple.comhttps://webkit.org/blog/8923/debugging-media-in-web-inspector/).

###### Use Mp4 Video Instead of Animated Gifs

GIFs can be up to 12 times as expensive in bandwidth and twice as expensive in energy use when compared to a modern video codec. Instead, use H.264-encoded MP4 files for animations; for example:

```javascript
<img src="explosion.mp4" alt="An explosion of colors.">

```

By placing your videos in `<img>` elements, the content loads faster, uses less battery power, and gets better performance.

To maintain compatibility with other web browsers, also include a fallback image:

```javascript
<picture>
    <source srcset="explosion.mp4" type="video/mp4">
    <img src="explosion.jpg" alt="An image of an explosion.">
</picture>
```

##### Select Playback Controls for Your Video

Use the best playback mode and controls for your video, depending on what type of content you are playing in your webpage.

###### Enable Inline Video Playback

When you want to display short-form content, it is more optimal to play your video inline. Use `<video playsinline>` to play videos inline.

Without the `playsinline` attribute, videos must be in full-screen mode for playback on iPhone. If videos do play in full-screen mode, they will continue to play inline when the user exits full-screen mode, even if the video element doesn’t contain the `playsinline` property.

###### Enable Full Screen Video Playback

When you want to display long-form content, it is more optimal to display your video in full-screen mode. On iPhone, when users play a video, they enter full screen automatically, unless inline playback has been explicitly specified. For all other platforms, if you use the video element’s default playback controls, the full-screen button is always available.

If, however, you want to add custom playback controls to your video element, you can specify custom UI controls that trigger full-screen behavior. To enter or exit full-screen mode, use [`webkitEnterFullscreen`](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1633500-webkitenterfullscreen) and [`webkitExitFullscreen`](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1629468-webkitexitfullscreen).

To see all full-screen functions in the API, see Displaying Video Fullscreen. To add additional playback controls for Picture in Picture and AirPlay, see [`Adding Picture in Picture to your Safari media controls`](https://developer.apple.com/documentation/webkitjs/adding_picture_in_picture_to_your_safari_media_controls) and [`Adding an AirPlay button to your Safari media controls`](https://developer.apple.com/documentation/webkitjs/adding_an_airplay_button_to_your_safari_media_controls).

###### Add Webrtc Playback Controls

WebRTC is also available for video broadcasting and conferencing in Safari. There is an expectation when joining a conference or webinar, that any remote video autoplays.

For a two-way video conference, video automatically plays after the user accepts the prompt requesting camera access.

However, for a one-way video conferencing scenario, such as a webinar, the user does not give explicit permission to the camera. Without a user gesture to indicate playback, the video cannot start. Add a play button to your media controls for one-way WebRTC experiences, so the user can start the video.

For more details on WebRTC, see [`Announcing WebRTC and Media Capture`](https://developer.apple.comhttps://webkit.org/blog/7726/announcing-webrtc-and-media-capture/) and [`A Closer Look into WebRTC`](https://developer.apple.comhttps://webkit.org/blog/7763/a-closer-look-into-webrtc/).

## See Also

- [Adding an AirPlay button to your Safari media controls](../webkitjs/adding_an_airplay_button_to_your_safari_media_controls.md)
  Create a custom control that adds AirPlay to your Safari media player. 
- [Adding Picture in Picture to your Safari media controls](../webkitjs/adding_picture_in_picture_to_your_safari_media_controls.md)
  Create a custom control that adds Picture in Picture to your Safari media player. 
- [Optimizing Your Website for Safari](optimizing-your-website-for-safari.md)
  Improve your website by optimizing it for Safari.
- [Promoting Apps with Smart App Banners](promoting-apps-with-smart-app-banners.md)
  Create a banner to promote your app on the App Store from a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/delivering-video-content-for-safari)*