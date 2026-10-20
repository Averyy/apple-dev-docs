# init(imageName:symbolName:location:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes an instance with a binary image name, source code location, and symbol name.

## Declaration

```swift
init(imageName: String, symbolName: String, location: XCTSourceCodeLocation?)
```

```objc
- (instancetype) initWithImageName:(NSString *) imageName symbolName:(NSString *) symbolName location:(XCTSourceCodeLocation *) location;
```

## Parameters

- `imageName`: A string that represents the name of the binary image containing the symbolicated code.
- `symbolName`: A string that represents a human-readable symbol in source code.
- `location`: A representation of a location in source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodesymbolinfo/init(imagename:symbolname:location:))*