# File System Events

**Framework**: Core Services  
**Role**: API Collection

Get notifications when the contents of a directory hierarchy change.

#### Overview

The file system events API provides a way for your application to ask for notification when the contents of a directory hierarchy are modified. For example, your application can use this to quickly detect when the user modifies a file within a project bundle using another application.

It also provides a lightweight way to determine whether the contents of a directory hierarchy have changed since your application last examined them. For example, a backup application can use this to determine what files have changed since a given time stamp or a given event ID.

## Topics

### Functions
- [func FSEventStreamCopyDescription(ConstFSEventStreamRef) -> CFString](./api-1442676-fseventstreamcopydescription.md)
- [func FSEventStreamCopyPathsBeingWatched(ConstFSEventStreamRef) -> CFArray](./api-1447917-fseventstreamcopypathsbeingwatch.md)
- [func FSEventStreamCreate(CFAllocator?, FSEventStreamCallback, UnsafeMutablePointer<FSEventStreamContext>?, CFArray, FSEventStreamEventId, CFTimeInterval, FSEventStreamCreateFlags) -> FSEventStreamRef?](./api-1443980-fseventstreamcreate.md)
- [func FSEventStreamCreateRelativeToDevice(CFAllocator?, FSEventStreamCallback, UnsafeMutablePointer<FSEventStreamContext>?, dev_t, CFArray, FSEventStreamEventId, CFTimeInterval, FSEventStreamCreateFlags) -> FSEventStreamRef?](./api-1447341-fseventstreamcreaterelativetodev.md)
- [func FSEventStreamFlushAsync(FSEventStreamRef) -> FSEventStreamEventId](./api-1441727-fseventstreamflushasync.md)
- [func FSEventStreamFlushSync(FSEventStreamRef)](./api-1445629-fseventstreamflushsync.md)
- [func FSEventStreamGetDeviceBeingWatched(ConstFSEventStreamRef) -> dev_t](./api-1449675-fseventstreamgetdevicebeingwatch.md)
- [func FSEventStreamGetLatestEventId(ConstFSEventStreamRef) -> FSEventStreamEventId](./api-1446030-fseventstreamgetlatesteventid.md)
- [func FSEventStreamInvalidate(FSEventStreamRef)](./api-1446990-fseventstreaminvalidate.md)
- [func FSEventStreamRelease(FSEventStreamRef)](./api-1445989-fseventstreamrelease.md)
- [func FSEventStreamRetain(FSEventStreamRef)](./api-1444986-fseventstreamretain.md)
- [func FSEventStreamScheduleWithRunLoop(FSEventStreamRef, CFRunLoop, CFString)](./api-1447824-fseventstreamschedulewithrunloop.md)
- [func FSEventStreamSetDispatchQueue(FSEventStreamRef, dispatch_queue_t?)](./api-1444164-fseventstreamsetdispatchqueue.md)
  Schedules the stream on the specified dispatch queue.
- [func FSEventStreamSetExclusionPaths(FSEventStreamRef, CFArray) -> Bool](./api-1444666-fseventstreamsetexclusionpaths.md)
- [func FSEventStreamShow(ConstFSEventStreamRef)](./api-1444302-fseventstreamshow.md)
- [func FSEventStreamStart(FSEventStreamRef) -> Bool](./api-1448000-fseventstreamstart.md)
- [func FSEventStreamStop(FSEventStreamRef)](./api-1447673-fseventstreamstop.md)
- [func FSEventStreamUnscheduleFromRunLoop(FSEventStreamRef, CFRunLoop, CFString)](./api-1441982-fseventstreamunschedulefromrunlo.md)
- [func FSEventsCopyUUIDForDevice(dev_t) -> CFUUID?](./api-1444453-fseventscopyuuidfordevice.md)
- [func FSEventsGetCurrentEventId() -> FSEventStreamEventId](./api-1442917-fseventsgetcurrenteventid.md)
- [func FSEventsGetLastEventIdForDeviceBeforeTime(dev_t, CFAbsoluteTime) -> FSEventStreamEventId](./api-1449772-fseventsgetlasteventidfordeviceb.md)
- [func FSEventsPurgeEventsForDeviceUpToEventId(dev_t, FSEventStreamEventId) -> Bool](./api-1447985-fseventspurgeeventsfordeviceupto.md)
### Enumerations
- [FSEventStreamCreateFlags](./file_system_events/api-1455376-fseventstreamcreateflags.md)
- [FSEventStreamEventFlags](./file_system_events/api-1455361-fseventstreameventflags.md)
- [FSEventStreamCreateFlags](./api-1455376-fseventstreamcreateflags.md)
- [FSEventStreamEventFlags](./api-1455361-fseventstreameventflags.md)
### Data Types
- [typealias FSEventStreamCallback](./fseventstreamcallback.md)
- [typealias FSEventStreamCreateFlags](./fseventstreamcreateflags.md)
- [typealias FSEventStreamEventFlags](./fseventstreameventflags.md)
- [typealias FSEventStreamEventId](./fseventstreameventid.md)
- [typealias FSEventStreamRef](./fseventstreamref.md)
### Constants
- [var kFSEventStreamEventExtendedDataPathKey: String](./kfseventstreameventextendeddatapathkey.md)
- [var kFSEventStreamEventExtendedFileIDKey: String](./kfseventstreameventextendedfileidkey.md)

## See Also

### Related Documentation
- [File System Events Programming Guide](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005289)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_system_events)*