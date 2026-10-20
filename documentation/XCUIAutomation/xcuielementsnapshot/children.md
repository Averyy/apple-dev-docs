# children

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of descendant user interface element snapshots.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
var children: [any XCUIElementSnapshot] { get }
```

```objc
@property (readonly) NSArray<id<XCUIElementSnapshot>> * children;
```

## See Also

### Inspecting attributes
- [var dictionaryRepresentation: [XCUIElement.AttributeName : Any]](./dictionaryrepresentation.md)
  A hierarchical dictionary representation of an element’s attributes, and all of an element’s user interface descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshot/children)*