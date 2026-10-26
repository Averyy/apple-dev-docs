# XCTContext

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

A proxy for the current testing context.

## Declaration

```swift
class XCTContext
```

```objc
@interface XCTContext : NSObject
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](./adding-attachments-to-tests-activities-and-issues.md)
- [Grouping Tests into Substeps with Activities](./grouping-tests-into-substeps-with-activities.md)

#### Overview

`XCTContext` provides a way for activities ([`XCTActivity`](./xctactivity.md)) to run against the current testing context, either directly in a test case or in custom testing utilities. You can break up long test methods in UI tests or integration tests into activities to reuse, and to simplify results in the Xcode test reports. Use [`runActivity(named:block:)`](./xctcontext/runactivity%28named,block%29.md) to run a block of code as a named substep in a test. For more information, see [Grouping Tests into Substeps with Activities](./grouping-tests-into-substeps-with-activities.md).

## Topics

### Running Activities
- [class func runActivity<Result>(named: String, block: (any XCTActivity) throws -> Result) rethrows -> Result](./xctcontext/runactivity%28named,block%29.md)
  Creates and runs an activity with the provided block of code.
- [+ runActivityNamed:block:](./xctcontext/runactivitynamed_block_.md)
  Creates and runs an activity with the provided block of code.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Activities
- [Grouping Tests into Substeps with Activities](./grouping-tests-into-substeps-with-activities.md)
  Simplify test reports by creating activities that organize substeps within complex test methods.
- [protocol XCTActivity](./xctactivity.md)
  A named substep of a test method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctcontext)*