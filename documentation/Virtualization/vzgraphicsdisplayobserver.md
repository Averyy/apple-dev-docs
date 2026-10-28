# VZGraphicsDisplayObserver

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

A protocol you implement to observe state changes in graphic displays.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol VZGraphicsDisplayObserver : NSObjectProtocol
```

```objc
@protocol VZGraphicsDisplayObserver <NSObject>
```

## Overview

Implement the methods in this protocol to observe and react to display reconfiguration.

## Topics

### Reacting to changes in display configuration
- [func displayDidBeginReconfiguration(VZGraphicsDisplay)](./vzgraphicsdisplayobserver/displaydidbeginreconfiguration%28_%29.md)
  The method the framework calls when the reconfiguration operation has begun.
- [func displayDidEndReconfiguration(VZGraphicsDisplay)](./vzgraphicsdisplayobserver/displaydidendreconfiguration%28_%29.md)
  The method the framework calls when the reconfiguration operation ends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing changes to the display configuration
- [func addObserver(any VZGraphicsDisplayObserver)](./vzgraphicsdisplay/addobserver%28_%29.md)
  Adds an observer to notify about display configuration changes.
- [func removeObserver(any VZGraphicsDisplayObserver)](./vzgraphicsdisplay/removeobserver%28_%29.md)
  Removes a display configuration change observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplayobserver)*