# Configuring a WatchKit Scene in a Storyboard

**Framework**: Watchkit

Xcode lets you configure information about your SpriteKit Scene in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

## Overview

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Scene'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The SpriteKit scene to be displayed. You can also set this value programmatically using the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSKScene/scene'}, {'type': 'text', 'text': ' property.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Frame Rate', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The desired frame rate for the scene’s animation. You can also set this value programmatically using the ', 'type': 'text'}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSKScene/preferredFramesPerSecond', 'isActive': True, 'type': 'reference'}, {'text': ' property.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Paused'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'A checkbox indicating whether the scene is paused. If checked, the scene’s content is fixed onscreen. No actions are executed and no physics simulation is performed. You can also configure this value programmatically using the ', 'type': 'text'}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSKScene/isPaused', 'type': 'reference', 'isActive': True}, {'text': ' property.', 'type': 'text'}]}] |

By default, when a watchOS app is running, the system reserves a strip of space across the top of the screen to display the time. The app’s content is only displayed in the area below the time.

In watchOS 4 and later, SpriteKit and SceneKit scenes can fill the full screen. When full screen mode is enabled, the SpriteKit or SceneKit scene extends up, under the time. The system still displays the time in the upper-right corner with a gradient behind it, making it clearly visible against the scene.

To enable full screen mode, place a SpriteKit or SceneKit scene as the interface controller’s only content. Then, in the interface controller’s Attribute inspector, enable the Full Screen attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/configuring-a-watchkit-scene-in-a-storyboard)*