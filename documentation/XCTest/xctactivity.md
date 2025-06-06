# XCTActivity

**Framework**: Xctest  
**Kind**: protocol

A named substep of a test method.

## Declaration

```swift
protocol XCTActivity : NSObjectProtocol
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)

## Topics

### Adding Attachments
- [func add(XCTAttachment)](xctactivity/add(_:).md)
  Associates a file, image, or other attachment with the activity.
### Activity Properties
- [var name: String](xctactivity/name.md)
  A human-readable name for the activity.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [XCTestCase](xctestcase.md)

## See Also

- [Grouping Tests into Substeps with Activities](grouping-tests-into-substeps-with-activities.md)
  Simplify test reports by creating activities that organize substeps within complex test methods.
- [class XCTContext](xctcontext.md)
  A proxy for the current testing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctactivity)*