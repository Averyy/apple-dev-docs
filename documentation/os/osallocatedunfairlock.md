# OSAllocatedUnfairLock

**Framework**: os  
**Kind**: struct

A structure that creates an unfair lock.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@frozen
struct OSAllocatedUnfairLock<State>
```

#### Overview

Unfair locks are low-level locks that block efficiently on contention. They’re useful for protecting code that loads stored resources. However, it’s unsafe to use [`os_unfair_lock`](os_unfair_lock.md) from Swift because it’s a value type and, therefore, doesn’t have a stable memory address. That means when you call [`os_unfair_lock_lock`](os_unfair_lock_lock.md) or [`os_unfair_lock_unlock`](os_unfair_lock_unlock.md) and pass a lock object using the `&` operator, the system may lock or unlock the wrong object.

Instead, use [`OSAllocatedUnfairLock`](osallocatedunfairlock.md), which avoids that pitfall because it doesn’t function as a value type, despite being a structure. All copied instances of an [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) control the same underlying lock allocation.

> ❗ **Important**:  If you’ve existing Swift code that uses [`os_unfair_lock`](os_unfair_lock.md), change it to use [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) to ensure correct locking behavior.

 If you’ve existing Swift code that uses [`os_unfair_lock`](os_unfair_lock.md), change it to use [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) to ensure correct locking behavior.

To create a lock that protects operation state, create an enumeration that contains the possible states, then create a lock object, passing the initial state. Here’s an example of what that looks like for an asset load operation:

```swift
enum MyState {
    case idle
    case loading
    case complete(MyAsset)
    case error(Error)
}
let protectedState = OSAllocatedUnfairLock(initialState: MyState.idle)
```

Storing the state inside the lock helps track what the lock is protecting, and provides a way to safely access the state. To begin using the lock, call `withLock(_:)` or `withLockIfAvailable(_:)`, passing a closure that contains the code for the lock to protect, like in the following example:

```swift
func myLoadMethod() {
    protectedState.withLock { state in
        state = .loading
    }
    var (resource, error) = loadMyResources()
    if resource != nil {
        protectedState.withLock { state in
            state = .complete(resource)
        }
    } else {
        protectedState.withLock { state in
            state = .error(error!)
        }
    }
}
```

To protect an operation with an externally defined state or no state, create a lock object without specifying an initial state. Nonscoped locking is more flexible, but offers no assistance in tracking the state of the operation the lock protects. To use a nonscoped lock, use `withLock(_:)` or `withLockIfAvailable(_:)`.

```swift
let myLock = OSAllocatedUnfairLock()
myLock.withLock {
    // Code that needs protection.
}
```

You can also use [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) with the more traditional lock/unlock approach by calling [`lock()`](osallocatedunfairlock/lock().md) before executing code that needs protection, and [`unlock()`](osallocatedunfairlock/unlock().md) upon completion, like this:

```swift
myLock.lock()
// Code that needs protection.
myLock.unlock()
```

When using this approach, you must call [`unlock()`](osallocatedunfairlock/unlock().md) from the same thread you use to call [`lock()`](osallocatedunfairlock/lock().md). Because of this, it’s unsafe to use this approach across an `await` suspension point. When using a lock with asynchronous code, lock using a closure or, even better, consider using an [`Actor`](https://developer.apple.com/documentation/Swift/Actor).

> ⚠️ **Warning**:  [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) isn’t a recursive lock. Attempting to lock an object more than once from the same thread without unlocking in between triggers a runtime exception.

 [`OSAllocatedUnfairLock`](osallocatedunfairlock.md) isn’t a recursive lock. Attempting to lock an object more than once from the same thread without unlocking in between triggers a runtime exception.

## Topics

### Creating a lock object
- [init()](osallocatedunfairlock/init.md)
  Creates a lock object that doesn’t protect state data.
- [init(initialState: State)](osallocatedunfairlock/init(initialstate:).md)
  Creates a lock object that maintains and protects state data.
### Using locks
- [func lock()](osallocatedunfairlock/lock.md)
  Acquires a lock.
- [func lockIfAvailable() -> Bool](osallocatedunfairlock/lockifavailable.md)
  Attempts to acquire a lock.
- [func unlock()](osallocatedunfairlock/unlock.md)
  Ends the lock.
### Determining lock ownership
- [OSAllocatedUnfairLock.Ownership](osallocatedunfairlock/ownership.md)
  An enumeration that represents the ownership status of an unfair lock.
- [func precondition(OSAllocatedUnfairLock<State>.Ownership)](osallocatedunfairlock/precondition(_:).md)
  Asserts if the lock object fails to meet specified ownership requirements.
### Initializers
- [init(uncheckedState: State)](osallocatedunfairlock/init(uncheckedstate:).md)
### Instance Methods
- [func lock(flags: OSAllocatedUnfairLockFlags)](osallocatedunfairlock/lock(flags:).md)
- [func withLock<R>((inout State) throws -> R) rethrows -> R](osallocatedunfairlock/withlock(_:)-1uy7m.md)
- [func withLock<R>(() throws -> R) rethrows -> R](osallocatedunfairlock/withlock(_:)-hple.md)
- [func withLock<R>(flags: OSAllocatedUnfairLockFlags, (inout State) throws -> R) rethrows -> R](osallocatedunfairlock/withlock(flags:_:)-1ub4c.md)
- [func withLock<R>(flags: OSAllocatedUnfairLockFlags, () throws -> R) rethrows -> R](osallocatedunfairlock/withlock(flags:_:)-u2xj.md)
- [func withLockIfAvailable<R>(() throws -> R) rethrows -> R?](osallocatedunfairlock/withlockifavailable(_:)-1rp3w.md)
- [func withLockIfAvailable<R>((inout State) throws -> R) rethrows -> R?](osallocatedunfairlock/withlockifavailable(_:)-3kw0o.md)
- [func withLockIfAvailableUnchecked<R>((inout State) throws -> R) rethrows -> R?](osallocatedunfairlock/withlockifavailableunchecked(_:)-15q0y.md)
- [func withLockIfAvailableUnchecked<R>(() throws -> R) rethrows -> R?](osallocatedunfairlock/withlockifavailableunchecked(_:)-6gji7.md)
- [func withLockUnchecked<R>((inout State) throws -> R) rethrows -> R](osallocatedunfairlock/withlockunchecked(_:)-7qywq.md)
- [func withLockUnchecked<R>(() throws -> R) rethrows -> R](osallocatedunfairlock/withlockunchecked(_:)-9v03m.md)
- [func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, (inout State) throws -> R) rethrows -> R](osallocatedunfairlock/withlockunchecked(flags:_:)-8cv64.md)
- [func withLockUnchecked<R>(flags: OSAllocatedUnfairLockFlags, () throws -> R) rethrows -> R](osallocatedunfairlock/withlockunchecked(flags:_:)-9iq8s.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock)*