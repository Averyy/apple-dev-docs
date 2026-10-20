# XCTActivity

**Framework**: XCTest  
**Kind**: protocol  
**Role**: Protocol

A named substep of a test method.

## Declaration

```swift
protocol XCTActivity : NSObjectProtocol
```

```objc
@protocol XCTActivity <NSObject>
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](./adding-attachments-to-tests-activities-and-issues.md)

## Topics

### Adding Attachments
- [func add(XCTAttachment)](./xctactivity/add%28_%29.md)
  Associates a file, image, or other attachment with the activity.
### Activity Properties
- [var name: String](./xctactivity/name.md)
  A human-readable name for the activity.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [XCTestCase](./xctestcase.md)

## See Also

### Activities
- [Grouping Tests into Substeps with Activities](./grouping-tests-into-substeps-with-activities.md)
  Simplify test reports by creating activities that organize substeps within complex test methods.
- [class XCTContext](./xctcontext.md)
  A proxy for the current testing context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctactivity)*