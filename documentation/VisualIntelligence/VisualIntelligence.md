# Visual Intelligence

**Framework**: Visual Intelligence  
**Kind**: module

Include your app’s content in search results that visual intelligence provides.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 27.0+ (Beta)

#### Overview

![The visual intelligence icon in front of a colorful background.](https://docs-assets.developer.apple.com/published/6c154d4425cad257aeab4750270dc624/visual-intelligence%402x.png)

People use visual intelligence to learn about places and objects around them and onscreen. By pointing their visual intelligence camera at their surroundings and tapping the search button, or by selecting objects in a screenshot, people can search for matching content in apps that offer integration with visual intelligence. Matches appear in the visual intelligence experience, allowing people to view and open items, or see additional search results in the corresponding app. For example, an app that provides information about landmarks can integrate with visual intelligence to allow people to view information about a landmark or open the app for more information.

To integrate your app with visual intelligence and include your app’s content in search results, use the Visual Intelligence framework and [`App Intents`](https://developer.apple.com/documentation/AppIntents). The Visual Intelligence framework provides you with information captured by visual intelligence, and your app uses the App Intents framework to receive the information and return matching content to the system and visual intelligence.

## Topics

### Essentials
- [Visual Intelligence updates](../Updates/VisualIntelligence.md)
  Learn about important changes in Visual Intelligence.
### Search integration
- [Integrating your app with visual intelligence](integrating-your-app-with-visual-intelligence.md)
  Enable people to find app content that matches their surroundings or objects onscreen with visual intelligence.
- [Adopting App Intents to support system experiences](../AppIntents/adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities so people can use your app’s content and actions across system experiences.
- [struct SemanticContentDescriptor](semanticcontentdescriptor.md)
  A type that represents a scene that visual intelligence captures, for example, a screenshot, photo, or photo and video stream.
### App Intents essentials
- [Creating your first app intent](../AppIntents/Creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/VisualIntelligence)*