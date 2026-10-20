# dictionaryRepresentation

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A hierarchical dictionary representation of an element’s attributes, and all of an element’s user interface descendants.

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
var dictionaryRepresentation: [XCUIElement.AttributeName : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * dictionaryRepresentation;
```

## See Also

### Inspecting attributes
- [var children: [any XCUIElementSnapshot]](./children.md)
  An array of descendant user interface element snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshot/dictionaryrepresentation)*