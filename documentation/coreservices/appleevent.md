# AppleEvent

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

A descriptor whose data is a list of descriptors containing both attributes and parameters that make up an Apple event.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AppleEvent = AERecord
```

```c
typedef AERecord AppleEvent;
```

#### Discussion

The Apple event data type describes a full-fledged Apple event. Like the data for an Apple event record (data type [`AERecord`](./aerecord.md)), the data for an Apple event consists of a list of keyword-specified descriptors. Unlike an Apple event record, the data for an Apple event is conceptually divided into two parts, one for attributes and one for parameters. This division within the Apple event allows the Apple Event Manager to distinguish between an event’s attributes and its parameters.

Many functions work with Apple events, including the functions described in [Apple Event Manager](../applicationservices/apple_event_manager.md), [Apple Event Manager](../applicationservices/apple_event_manager.md), [Creating an Apple Event](../applicationservices/apple_event_manager.md#1651538), and [Sending an Apple Event](../applicationservices/apple_event_manager.md#1652529). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/appleevent)*