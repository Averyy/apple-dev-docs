# assert_wait_timeout

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
wait_result_t assert_wait_timeout(event_t event, wait_interrupt_t interruptible, uint32_t interval, uint32_t scale_factor);
```

## See Also

- [Assert](1574809-assert.md)
- [assert_wait](1524384-assert_wait.md)
- [assert_wait_deadline](1524378-assert_wait_deadline.md)
- [assert_wait_deadline_with_leeway](1524380-assert_wait_deadline_with_leeway.md)
- [assert_wait_timeout_with_leeway](1524381-assert_wait_timeout_with_leeway.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1524367-assert_wait_timeout)*