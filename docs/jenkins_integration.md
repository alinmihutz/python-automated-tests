### Requirements:
* [hmtlpublisher](https://plugins.jenkins.io/htmlpublisher)
* [junit](https://plugins.jenkins.io/junit)
* [Groovy Postbuild Plugin](http://wiki.jenkins-ci.org/display/JENKINS/Groovy+Postbuild+Plugin)
* [Pipeline+Groovy+Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Pipeline+Groovy+Plugin)

### Build Configuration

Check list:
* install requirements
* create a Freestyle project build
* use custom workspace ?
![custom-workspace](images/jenkins/custom-workspace.png)
* execute shell build

````
#!c:\cygwin64\bin\bash
python /core/app/Main.py
````

* configure post build actions

### Post build actions:

* publish-xml-reports
![publish-xml-reports](images/jenkins/publish-xml-reports.png)

* publish-html-reports
![publish-html-reports](images/jenkins/publish-html-reports.png)

* groovy-postbuild
![groovy-postbuild](images/jenkins/groovy-postbuild.png)

```
errpattern = ~/FAILED/;

manager.build.logFile.eachLine { line ->
    errmatcher = errpattern.matcher(line)
    if (errmatcher.find()) {
        manager.buildFailure()
    }
}
```

### Notes
CSS may be striped because of the Content Security Policy in Jenkins

Manage Jenkins > Script console

````bash
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
````
