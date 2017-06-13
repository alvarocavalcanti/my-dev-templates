# Java-related Configuration and Tips

## Gradle

### Test output task

```java
import org.gradle.api.tasks.testing.logging.TestExceptionFormat
import org.gradle.api.tasks.testing.logging.TestLogEvent

tasks.withType(Test) {
    testLogging {
        // set options for log level LIFECYCLE
        events "passed", "skipped", "failed", "standardOut"
        showExceptions true
        exceptionFormat "full"
        showCauses true
        showStackTraces true

        // set options for log level DEBUG and INFO
        debug {
            events "started", "passed", "skipped", "failed", "standardOut", "standardError"
            exceptionFormat "full"
        }
        info.events = debug.events
        info.exceptionFormat = debug.exceptionFormat

        afterSuite { desc, result ->
            if (!desc.parent) { // will match the outermost suite
                def output = "Results: ${result.resultType} (${result.testCount} tests, ${result.successfulTestCount} successes, ${result.failedTestCount} failures, ${result.skippedTestCount} skipped)"
                def startItem = '|  ', endItem = '  |'
                def repeatLength = startItem.length() + output.length() + endItem.length()
                println('\n' + ('-' * repeatLength) + '\n' + startItem + output + endItem + '\n' + ('-' * repeatLength))
            }
        }
    }
}
```

### Output Example

```bash
io.klever.user.svc.UserControllerV2Test > savesNewsUserAndSendsPassword SKIPPED

io.klever.user.TranslatorTest > createsTranslatorWithBasicInfo PASSED

io.klever.user.TranslatorTest > createsTranslatorWithRandomPassword PASSED

io.klever.user.TranslatorTest > createsTranslatorWithBlankPassword PASSED

io.klever.user.UserTest > createsUserWithBasicInfo PASSED

io.klever.user.UserTest > createsEmptyUserWithTimestampValues PASSED

io.klever.user.UserTest > activatesTheUser PASSED

io.klever.user.UserTest > createsUserWithGivenCredentialsInfo PASSED

io.klever.util.memsource.JobPartProgressMonitorTest > testFindReviewJobPartsWithSuccess PASSED

----------------------------------------------------------------------
|  Results: SUCCESS (15 tests, 14 successes, 0 failures, 1 skipped)  |
----------------------------------------------------------------------

BUILD SUCCESSFUL

```
