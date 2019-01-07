<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<form action="javascript:code_toggle()">
  <input type="submit" id="toggleButton" value="Show Code">
</form>

```python
from bokeh.plotting import figure, output_notebook, show
output_notebook()
```



    <div class="bk-root">
        <a href="https://bokeh.pydata.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
        <span id="1001">Loading BokehJS ...</span>
    </div>




# Google Sans [Localization]

**Scope**: [localized version] extension of the Google Sans typeface

**Phase**: Planning, Design, Engineering, Release

**Start Date**: 1/1/18

**Proposed End Date**: 6/1/20

**Estimated End Date**: 6/1/20

**Development Team**:
  - Team member 1 (role) (contact email)
  - Team member 2 (role) (contact email)
  



## Schedule Performance

### Current Milestone

**Title**: [milestone title]

**Associated Documentation**: [URL]

[INSERT GANTT CHART FOR MILESTONE HERE]

**Begin Date**: 12/1/00

**Proposed End Date**: 1/1/01

**Estimated End Date**: 2/1/01

**Variance Narrative**: [Free text or N/A]

**Corrective Action Plan**: [Free text or N/A]

- cause of variance
- impact of variance
- need to rebaseline schedule and modify estimated end date above


### Next Milestone

**Title**: [milestone title]

**Proposed Start Date**: 2/2/01

**Estimated Start Date**: 2/2/01



## Work Effort


```python
x = [1,2,3]
y = [4,5,6]

p = figure()
p.line(x,y)

show(p)
```








  <div class="bk-root" id="81a2aaea-f301-4492-8ac5-e91cf98d856e" data-root-id="1002"></div>





### Respository Commits / Week Over the Last 4 Weeks


```python
x = [1,2,3,4]
y = [8,9,10,8]

plot = figure()
plot.vbar(x, top=y, color="blue", width=0.5)

show(plot)
```








  <div class="bk-root" id="5741c9fe-681b-4e80-ad36-388bca840492" data-root-id="1104"></div>





### Commits in the Last [X PERIOD]


[pull repository with git and print the git log with titles for the repository commits in the last X days]


```
84ebd94 - Thu Jun 7 09:51:05 2018 -0400, 2 days ago : [README.md] updated new bug reporting URL
cdf4a0d - Sun Jun 3 22:10:58 2018 -0400, 6 days ago : added link to crunch executable upgrade shell script gist
fc885d6 - Sun Jun 3 22:05:34 2018 -0400, 6 days ago : Merge branch 'dev' into master-merge
4030331 - Sun Jun 3 21:59:28 2018 -0400, 6 days ago : added upgrade documentation
e8084b4 - Sun Jun 3 21:44:50 2018 -0400, 6 days ago : macOS GUI installer v3.0.0
139284e - Sun Jun 3 21:44:27 2018 -0400, 6 days ago : crunch executable v3.0.0
e2d8dab - Sun Jun 3 21:44:13 2018 -0400, 6 days ago : macOS GUI v3.0.0
1b3142e - Sun Jun 3 21:39:45 2018 -0400, 6 days ago : fixed test with new image size
c396812 - Sun Jun 3 21:26:07 2018 -0400, 6 days ago : updated optimized images

```

## Product Changelog

### New

- new glyph 1 with image at commit SHA1 hash
- new glyph 2 with image at commit SHA1 hash

### Modified

- glyph 1 with image at commit SHA1 hash
- glyph 2 with image at commit SHA1 hash

### Removed

- topic 1 at commit SHA1 hash
- topic 1 at commit SHA1 hash


## Product Quality Assessment

### Design QA

[Feedback from external audits/Google teams/etc]

### Technical/Engineering QA

[Font Bakery testing report]

### Integration QA

[Examples of changes in prototypes of common use situations]


## Communication and Decisions

### To Google Comms

- [X] CS to DC - this, OK'd by DC
- [X] CS to XX - that, OK'd by XX

### From Google Comms

- [X] DC to EE - this, OK'd by EE
- [X] DC to FF - that, OK'd by FF


## Action Items

- [ ] who - what - when
- [ ] who - what - when
- [ ] who - what - when


```python
import datetime
today = datetime.date.today()
print(today.strftime("Report generated on %b-%d-%Y"))
```

    Report generated on Jan-07-2019

