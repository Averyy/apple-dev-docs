# proc_sessionid

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
pid_t proc_sessionid(proc_t p);
```

## See Also

- [proc_best_name](3020681-proc_best_name.md)
- [proc_chrooted](1488999-proc_chrooted.md)
- [proc_csflags](3538582-proc_csflags.md)
- [proc_exiting](1489000-proc_exiting.md)
- [proc_find](1488987-proc_find.md)
- [proc_forcequota](1488993-proc_forcequota.md)
- [proc_gettty](3538583-proc_gettty.md)
- [proc_gettty_dev](3538584-proc_gettty_dev.md)
- [proc_in_teardown](2990533-proc_in_teardown.md)
- [proc_is64bit](1488977-proc_is64bit.md)
- [proc_is64bit_data](2967400-proc_is64bit_data.md)
- [proc_is_classic](1488982-proc_is_classic.md)
- [proc_isinferior](1489001-proc_isinferior.md)
- [proc_issetugid](2998888-proc_issetugid.md)
- [proc_issignal](1488967-proc_issignal.md)
- [proc_name](1488959-proc_name.md)
- [proc_noremotehang](1488981-proc_noremotehang.md)
- [proc_original_ppid](3325836-proc_original_ppid.md)
- [proc_pgrpid](1488969-proc_pgrpid.md)
  Get the process group id for the passed-in process.
- [proc_pid](1488997-proc_pid.md)
- [proc_platform](3194345-proc_platform.md)
- [proc_ppid](1488964-proc_ppid.md)
- [proc_rele](1488988-proc_rele.md)
- [proc_sdk](3194346-proc_sdk.md)
- [proc_self](1488975-proc_self.md)
- [proc_selfcsflags](1488989-proc_selfcsflags.md)
- [proc_selfname](1488979-proc_selfname.md)
- [proc_selfpgrpid](1488978-proc_selfpgrpid.md)
  Get the process group id for the current process, as with proc_pgrpid().
- [proc_selfpid](1488971-proc_selfpid.md)
- [proc_selfppid](1488985-proc_selfppid.md)
- [proc_send_synchronous_EXC_RESOURCE](3013826-proc_send_synchronous_exc_resour.md)
- [proc_signal](1488994-proc_signal.md)
- [proc_suser](1488961-proc_suser.md)
- [proc_tbe](1488984-proc_tbe.md)
- [proc_ucred](1488996-proc_ucred.md)
- [current_proc](1427365-current_proc.md)
- [current_proc_EXTERNAL](1488991-current_proc_external.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3366028-proc_sessionid)*