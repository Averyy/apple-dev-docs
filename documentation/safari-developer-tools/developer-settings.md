# Changing Developer settings in Safari on macOS

**Framework**: Safari Developer Features

Change developer-centric settings that change the behavior of Safari.

#### Overview

Once features for web developers are shown, Safari adds a **Developer** pane to its settings, from which several behaviors can be controlled.

##### Automation

- **Allow remote automation**: Allow Safari to be automatically controlled with [`WebDriver`](webdriver.md).
- **Allow JavaScript from Smart Search field**: Allow text starting with `javascript:` to be run on the current page when entered in the Smart Search field.
- **Allow JavaScript from Apple Events**: Allow JavaScript to be executed on webpages via [`AppleScript`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/index.html).

##### Compatibility

- **Disable site-specific quirks**: On rare occasions, when a particular website does not work correctly in Safari, modifications are made in browser code to get that site to work. This setting disables such modifications to make it possible for the site’s developers to debug their problem. If there are no site-specific quirks, this setting has no effect.

##### Security

- **Disable local file restrictions**: Disable security checks that may prohibit local development when loading content with the `file://` protocol.
- **Disable cross-origin restrictions**: Disable security checks that are performed when loading resources from origins other than the one from which the main page was loaded.

##### Privacy

- **Enable Intelligent Tracking Prevention debug mode**: Enable additional logging for Intelligent Tracking Prevention. [`Learn more about Intelligent Tracking Prevention debug mode…`](https://developer.apple.comhttps://webkit.org/blog/8387/itp-debug-mode-in-safari-technology-preview-62/)
- **Enable Private Click Measurement debug mode**: Enables sending reports after 10 seconds, instead of 24-48 hours, after an event, as well as enabling additional logging in Web Inspector’s console. [`Learn more about Private Click Measurement…`](https://developer.apple.comhttps://webkit.org/blog/11940/pcm-click-fraud-prevention-and-attribution-sent-to-advertiser/)

##### Extensions

- **Allow unsigned extensions**: Allow enabling unsigned extensions in the **Extensions** settings panel.  [`Learn more about allowing unsigned extensions.`](https://developer.apple.comhttps://developer.apple.com/documentation/safariservices/safari_web_extensions/running_your_safari_web_extension#3744467)

## See Also

- [Changing Feature Flag settings in Safari on macOS](feature-flag-settings.md)
  Test new web platform features before they ship in Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/developer-settings)*