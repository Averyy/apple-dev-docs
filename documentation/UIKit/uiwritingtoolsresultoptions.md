# UIWritingToolsResultOptions

**Framework**: UIKit  
**Kind**: struct

Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.4+

## Declaration

```swift
struct UIWritingToolsResultOptions
```

#### Overview

When configuring a text view, specify what type of text input you want Writing Tools to deliver to your view. You can ask it to return plain text without any attributes, or you can ask it to apply relevant formatting attributes to the text. You can even encourage it to return items in a list or format them in a table.

## Topics

### Getting the output options
- [static var plainText: UIWritingToolsResultOptions](uiwritingtoolsresultoptions/plaintext.md)
  An option to allow only plain text without any attributes in the returned text.
- [static var richText: UIWritingToolsResultOptions](uiwritingtoolsresultoptions/richtext.md)
  An option to include style attributes consistent with the RTF format in the returned text.
- [static var list: UIWritingToolsResultOptions](uiwritingtoolsresultoptions/list.md)
  An option to allow list-style formatting in the returned text.
- [static var table: UIWritingToolsResultOptions](uiwritingtoolsresultoptions/table.md)
  An option to allow tabular layout attributes in the returned text.
### Initializers
- [init(rawValue: UInt)](uiwritingtoolsresultoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md)
  Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [enum UIWritingToolsBehavior](uiwritingtoolsbehavior.md)
  Constants that specify the writing tools experience for the underlying view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions)*