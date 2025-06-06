# VZGraphicsDisplayObserver

**Framework**: Virtualization  
**Kind**: protocol

A protocol you implement to observe state changes in graphic displays.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol VZGraphicsDisplayObserver : NSObjectProtocol
```

#### Overview

Implement the methods in this protocol to observe and react to display reconfiguration.

## Topics

### Reacting to changes in display configuration
- [func displayDidBeginReconfiguration(VZGraphicsDisplay)](vzgraphicsdisplayobserver/displaydidbeginreconfiguration(_:).md)
  The method the framework calls when the reconfiguration operation has begun.
- [func displayDidEndReconfiguration(VZGraphicsDisplay)](vzgraphicsdisplayobserver/displaydidendreconfiguration(_:).md)
  The method the framework calls when the reconfiguration operation ends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/addobserver(_:).md)
  Adds an observer to notify about display configuration changes.
- [func removeObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/removeobserver(_:).md)
  Removes a display configuration change observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayobserver)*