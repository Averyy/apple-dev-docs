# interfaceProperty

**Framework**: Watchkit  
**Kind**: property

The name of the outlet in your interface controller to which the object is bound.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var interfaceProperty: String { get }
```

## Overview

The string in this property corresponds to the name of a property in one of your [`WKInterfaceController`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller) subclasses. WatchKit uses this value internally to manage the connection between the interface object and the corresponding object on Apple Watch. You do not need to use this property directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/interfaceproperty)*