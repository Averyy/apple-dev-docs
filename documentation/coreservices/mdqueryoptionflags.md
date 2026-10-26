# MDQueryOptionFlags

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Specify the execution mode for a query.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
struct MDQueryOptionFlags
```

```c
typedef enum MDQueryOptionFlags : unsigned int {
    ...
} MDQueryOptionFlags;
```

## Topics

### Constants
- [var kMDQuerySynchronous: MDQueryOptionFlags](./kmdquerysynchronous.md)
  Specifies that a query should block during the initial gather phase. The query’s run loop will run in the default mode. If this option is not specified the query function returns immediately after starting the query asynchronously.
- [var kMDQueryWantsUpdates: MDQueryOptionFlags](./kmdquerywantsupdates.md)
- [var kMDQueryAllowFSTranslation: MDQueryOptionFlags](./kmdqueryallowfstranslation.md)
- [kMDQuerySynchronous](./mdqueryoptionflags/kmdquerysynchronous.md)
  Specifies that a query should block during the initial gather phase. The query’s run loop will run in the default mode. If this option is not specified the query function returns immediately after starting the query asynchronously.
- [kMDQueryWantsUpdates](./mdqueryoptionflags/kmdquerywantsupdates.md)
- [kMDQueryAllowFSTranslation](./mdqueryoptionflags/kmdqueryallowfstranslation.md)
### Initializers
- [init(UInt32)](./mdqueryoptionflags/api-1443626-init.md)
- [init(rawValue: UInt32)](./mdqueryoptionflags/api-1444315-init.md)
### Instance Properties
- [var rawValue: UInt32](./mdqueryoptionflags/api-1448284-rawvalue.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdqueryoptionflags)*