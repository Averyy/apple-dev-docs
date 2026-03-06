# Changing Feature Flag settings in Safari on macOS

**Framework**: Safari Developer Features

Test new web platform features before they ship in Safari.

#### Overview

The web is constantly evolving with new features and technologies. It can be exciting to see potential future tools and technologies, and even more exciting to begin experimenting with them before they ship in web browsers.

Safari lets you enable these features using the new **Feature Flags** settings, which can be opened from the [`Develop menu`](develop-menu.md) by choosing **Feature Flags…**.

Features are organized by topic, like Animation, CSS, JavaScript, Media, and more, making it easy to find related features. They can also be searched by both feature name and status.

When you toggle a feature to a non-default state, its name is displayed in bold.

> ❗ **Important**: The default setting for each feature flag is how users will generally experience your content, so make sure your pages gracefully handle the absence of a feature you’ve enabled for development.

#### Feature Statuses

There are four possible statuses for a feature, each with a different meaning and default state. Non-developer features will typically start as **Testable** features, and then move to **Preview** as the feature and spec the feature is based on matures, eventually becoming **Stable** features.

- **Stable**: Stable features are features that have recently begun shipping in Safari and are on by default. These feature can be toggled to help determine if a feature is causing an issue, or to make sure your site still gracefully handles the absence of the feature for features not yet shipping in all browsers. Stable features will eventually be removed from the list of feature flags.
- **Preview**: Preview features are features that are ready for developers to begin experimenting with. While these features are disabled by default in Safari, they are enabled by default in [`Safari Technology Preview`](https://developer.apple.comhttps://developer.apple.com/safari/resources/).
- **Testable**: Testable features are those that are not ready for use, but that may be ready for early feedback. Testable features can help inform the standards the feature is based on to make sure the spec works for web developers. These features are disabled by default.
- **Developer**: Developer features can be settings that adjust the behavior of WebKit for development, reenable deprecated API for testing, or enable an extra tool like Media Stats. These features are disabled by default.

## See Also

- [Changing Developer settings in Safari on macOS](developer-settings.md)
  Change developer-centric settings that change the behavior of Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/feature-flag-settings)*