# XCTContext

**Framework**: XCTest  
**Kind**: class

A proxy for the current testing context.

## Declaration

```swift
class XCTContext
```

## Mentions

- [Grouping Tests into Substeps with Activities](grouping-tests-into-substeps-with-activities.md)
- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)

#### Overview

`XCTContext` provides a way for activities ([`XCTActivity`](xctactivity.md)) to run against the current testing context, either directly in a test case or in custom testing utilities. You can break up long test methods in UI tests or integration tests into activities to reuse, and to simplify results in the Xcode test reports. Use [`runActivity(named:block:)`](xctcontext/runactivity(named:block:).md) to run a block of code as a named substep in a test. For more information, see [`Grouping Tests into Substeps with Activities`](grouping-tests-into-substeps-with-activities.md).

## Topics

### Running Activities
- [class func runActivity<Result>(named: String, block: (any XCTActivity) throws -> Result) rethrows -> Result](xctcontext/runactivity(named:block:).md)
  Creates and runs an activity with the provided block of code.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Grouping Tests into Substeps with Activities](grouping-tests-into-substeps-with-activities.md)
  Simplify test reports by creating activities that organize substeps within complex test methods.
- [protocol XCTActivity](xctactivity.md)
  A named substep of a test method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctcontext)*