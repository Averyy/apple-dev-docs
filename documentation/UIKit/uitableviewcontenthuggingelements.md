# UITableViewContentHuggingElements

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that determine which types of items in a table view tightly hug their content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct UITableViewContentHuggingElements
```

```c
enum UITableViewContentHuggingElements : NSInteger;
```

## Topics

### Specifying content-hugging elements
- [static var sectionHeaders: UITableViewContentHuggingElements](./uitableviewcontenthuggingelements/sectionheaders.md)
  A mode where section headers in the table view tightly hug their content.
- [UITableViewContentHuggingElementsNone](./uitableviewcontenthuggingelements/uitableviewcontenthuggingelementsnone.md)
  A mode where none of the items in the table view tightly hug their content.
### Creating a content-hugging elements structure
- [init(rawValue: Int)](./uitableviewcontenthuggingelements/init%28rawvalue%29.md)
  Creates a content-hugging elements structure.

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

### Managing content-hugging behavior
- [var contentHuggingElements: UITableViewContentHuggingElements](./uitableview/contenthuggingelements.md)
  A setting that determines which type of items tightly hug their content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcontenthuggingelements)*