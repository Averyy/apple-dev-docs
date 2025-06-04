# WKSnapshotReason.appScheduled

**Framework**: Watchkit  
**Kind**: case

The app scheduled this snapshot.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case appScheduled
```

## Overview

You can schedule snapshots either by calling the [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](https://developer.apple.com/documentation/watchkit/wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:)) method, or—when completing a background task—by calling the [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)) method and passing [`true`](https://developer.apple.com/documentation/swift/true).

These snapshot refresh tasks are only triggered when the watchOS app is in the dock.

## See Also

- [WKSnapshotReason.appBackgrounded](appbackgrounded.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appbackgrounded))
- [WKSnapshotReason.complicationUpdate](complicationupdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/complicationupdate))
- [WKSnapshotReason.prelaunch](prelaunch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/prelaunch))
- [WKSnapshotReason.returnToDefaultState](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason/returntodefaultstate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotreason/appscheduled)*