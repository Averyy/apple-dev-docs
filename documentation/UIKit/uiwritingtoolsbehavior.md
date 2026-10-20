# UIWritingToolsBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the writing tools experience for the underlying view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
enum UIWritingToolsBehavior
```

```c
enum UIWritingToolsBehavior : NSInteger;
```

#### Overview

Writing tools provide proofreading and rewriting support for the content of text views. On devices that support writing tools features, people engage the system UI to choose how to rewrite all or part of the available text. These constants indicate whether people experience writing tools inline with their text, in an overlay panel, or not at all.

## Topics

### Getting the writing tools behaviors
- [UIWritingToolsBehavior.none](./uiwritingtoolsbehavior/none.md)
  An option to prevent the writing tools from modifying the text in the view.
- [UIWritingToolsBehavior.default](./uiwritingtoolsbehavior/default.md)
  An option to let the system determine the best way to enable writing tools for the view.
- [UIWritingToolsBehavior.complete](./uiwritingtoolsbehavior/complete.md)
  An option to provide the complete writing tools experience for the text view.
- [UIWritingToolsBehavior.limited](./uiwritingtoolsbehavior/limited.md)
  An option to provide a limited, overlay-panel experience for the text view.
### Initializers
- [init?(rawValue: Int)](./uiwritingtoolsbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuration
- [Customizing Writing Tools behavior for UIKit views](./customizing-writing-tools-behavior-for-system-views.md)
  Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [struct UIWritingToolsResultOptions](./uiwritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsbehavior)*