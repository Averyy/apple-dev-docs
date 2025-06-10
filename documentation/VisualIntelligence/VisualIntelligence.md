# Visual Intelligence

**Framework**: Visual Intelligence  
**Kind**: module

Include your app’s content in search results that visual intelligence provides.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

#### Overview

![The visual intelligence icon in front of a colorful background.](https://docs-assets.developer.apple.com/published/3bd1138a2956a5abd6c5ad786af48472/visual-intelligence%402x.png)

People use visual intelligence to learn about places and objects around them and onscreen. By pointing their visual intelligence camera at their surroundings and tapping the search button, or by selecting objects in a screenshot, people can search for matching content in apps that offer integration with visual intelligence. Matches appear in the visual intelligence experience, allowing people to view and open items, or see additional search results in the corresponding app. For example, an app that provides information about landmarks might integrate with visual intelligence to allow people to  view information about a landmark or open the app for more information.

To integrate your app with visual intelligence and include your app’s content in search results, use the Visual Intelligence framework and [`App Intents`](https://developer.apple.com/documentation/AppIntents). The Visual Intelligence framework provides you with information captured by visual intelligence, and your app uses the App Intents framework to receive the information and return matching content to the system and visual intelligence.

## Topics

### Essentials
- [Integrating your app with visual intelligence](integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [struct SemanticContentDescriptor](semanticcontentdescriptor.md)
  A type that represents a scene that visual intelligence captures, like a screenshot, photo, or photo and video stream.
### App intents essentials
- [Making actions and content discoverable and widely available](../AppIntents/Making-actions-and-content-discoverable-and-widely-available.md)
  Adopt App Intents to make your app discoverable with Spotlight, controls, widgets, and the Action button.
- [Creating your first app intent](../AppIntents/Creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/VisualIntelligence)*