# UIWritingToolsResultOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIWritingToolsResultOptions : NSUInteger;
```

## Overview

When configuring a text view, specify what type of text input you want Writing Tools to deliver to your view. You can ask it to return plain text without any attributes, or you can ask it to apply relevant formatting attributes to the text. You can even encourage it to return items in a list or format them in a table.

## Topics

### Getting the output options
- [static var plainText: UIWritingToolsResultOptions](./uiwritingtoolsresultoptions/plaintext.md)
  An option to allow only plain text without any attributes in the returned text.
- [static var richText: UIWritingToolsResultOptions](./uiwritingtoolsresultoptions/richtext.md)
  An option to include style attributes consistent with the RTF format in the returned text.
- [static var list: UIWritingToolsResultOptions](./uiwritingtoolsresultoptions/list.md)
  An option to allow list-style formatting in the returned text.
- [static var table: UIWritingToolsResultOptions](./uiwritingtoolsresultoptions/table.md)
  An option to allow tabular layout attributes in the returned text.
### Initializers
- [init(rawValue: UInt)](./uiwritingtoolsresultoptions/init%28rawvalue%29.md)
### Type Properties
- [static var presentationIntent: UIWritingToolsResultOptions](./uiwritingtoolsresultoptions/presentationintent.md)
  implies `RichText`, `List`, and `Table`, and Writing Tools may provide text with presentation intent attributes. Writing Tools will use `NSPresentationIntent` instead of `NSTextList` and `NSTextTable` to represent lists and tables.
### Enumeration Cases
- [UIWritingToolsResultDefault](./uiwritingtoolsresultoptions/uiwritingtoolsresultdefault.md)
  System-defined behavior

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Configuration
- [Customizing Writing Tools behavior for UIKit views](./customizing-writing-tools-behavior-for-system-views.md)
  Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [enum UIWritingToolsBehavior](./uiwritingtoolsbehavior.md)
  Constants that specify the writing tools experience for the underlying view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolsresultoptions)*