# assert_wait_timeout_with_leeway

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.9+

## Declaration

```c
wait_result_t assert_wait_timeout_with_leeway(event_t event, wait_interrupt_t interruptible, wait_timeout_urgency_t urgency, uint32_t interval, uint32_t leeway, uint32_t scale_factor);
```

## See Also

### Assertions
- [Assert](./api-1574809-assert.md)
- [assert_wait](./api-1524384-assert_wait.md)
- [assert_wait_deadline](./api-1524378-assert_wait_deadline.md)
- [assert_wait_deadline_with_leeway](./api-1524380-assert_wait_deadline_with_leeway.md)
- [assert_wait_timeout](./api-1524367-assert_wait_timeout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1524381-assert_wait_timeout_with_leeway)*