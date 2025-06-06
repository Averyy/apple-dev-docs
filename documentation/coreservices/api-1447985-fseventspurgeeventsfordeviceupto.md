# FSEventsPurgeEventsForDeviceUpToEventId(_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventsPurgeEventsForDeviceUpToEventId(_ dev: dev_t, _ eventId: FSEventStreamEventId) -> Bool
```

#### Return_value

True if it succeeds, otherwise False if it fails.

#### Discussion

Purges old events from the persistent per-volume database maintained by the service. Can only be called by the root user.

## Parameters

- `dev`: The dev_t of the device.
- `eventId`: The event ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447985-fseventspurgeeventsfordeviceupto)*