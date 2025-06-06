# Optimizing Your Website for Safari

**Framework**: Webkit

Improve your website by optimizing it for Safari.

#### Overview

Safari is a full-featured web browser that comes with macOS and iOS. While all W3C-compliant websites work in Safari, there are a few ways that you can optimizing your content for Safari to ensure it works great on Apple devices.

![Improve your website’s performance in Safari.](https://docs-assets.developer.apple.com/published/4fcae417fa1227eaf78ed2a685a93f6c/media-3030233%402x.png)

To ensure that your content works great in Safari:

-  Use Web Inspector and Safari Developer Tools to inspect details and test the performance of your website in Safari. See [`Safari Developer Help`](https://developer.apple.comhttps://support.apple.com/guide/safari-developer/welcome/mac).
-  Encode media content so that it loads quickly in Safari. For audio and video content, use the HTML5 markup elements `<audio>` and `<video>`, and use `<canvas>` for vector graphics and animation. See HLS Authoring Specification for Apple Devices.
-  To ensure that your website loads fast and efficiently, Safari does not rely on plug-ins to handle audio, video, or animation.
-  Use appropriate markup and tags to ensure the accessibility of your website, including [`ARIA`](https://developer.apple.comhttps://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) and [`A11Y`](https://developer.apple.comhttps://a11yproject.com).
-  Use responsive design to accommodate the many different Apple devices for iOS, macOS, and watchOS. A responsive design ensures that users can view your website in Safari everywhere, regardless of the screen or window width. See [`Designing Web Content for watchOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/239/), and [`Using Safari to Deliver and Debug a Responsive Web Design`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2015/505/).
-  Add support for Multi-Touch gestures so these interactions are easier for users on mobile devices.
-  Ensure that your website uses one of Safari’s supported security features, like subresource integrity, TLS, RSA, and HTTPS.
-  Make use of good web design practices and web standards. Make use of HTML5, CSS3, and the latest web standards supported by the [`W3C`](https://developer.apple.comhttps://www.w3.org).

> 💡 **Tip**:  Use feature detection to make your website browser independent. By detecting the browser, you can not only support multiple browsers but also support multiple WebKit versions.

 Use feature detection to make your website browser independent. By detecting the browser, you can not only support multiple browsers but also support multiple WebKit versions.

Additionally, you can customize rules for [`Applebot`](https://developer.apple.comhttps://support.apple.com/en-us/HT204683), the web crawler for Apple.

By implementing these best practices and testing your website in Safari, you ensure that visitors to your site have a great experience on all Apple devices.

## See Also

- [Delivering Video Content for Safari](delivering-video-content-for-safari.md)
  Improve the performance and appearance of video in your website in Safari.
- [Promoting Apps with Smart App Banners](promoting-apps-with-smart-app-banners.md)
  Create a banner to promote your app on the App Store from a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/optimizing-your-website-for-safari)*