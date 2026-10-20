# XCTMeasureOptions

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

Options to control the gathering of performance measurements during tests.

## Declaration

```swift
class XCTMeasureOptions
```

```objc
@interface XCTMeasureOptions : NSObject
```

## Topics

### Getting Default Options
- [class var `default`: XCTMeasureOptions](./xctmeasureoptions/default.md)
  The default measurement options.
### Using Option Details
- [var invocationOptions: XCTMeasureOptions.InvocationOptions](./xctmeasureoptions/invocationoptions-swift.property.md)
  Options that define whether measurement is automatically or manually controlled.
- [XCTMeasureOptions.InvocationOptions](./xctmeasureoptions/invocationoptions-swift.struct.md)
  Test measurement options that control how measurement starts and stops.
- [var iterationCount: Int](./xctmeasureoptions/iterationcount.md)
  The number of times the performance test measures its block.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmeasureoptions)*