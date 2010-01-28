<%inherit file="/layout/main.mako"/>

<table style="width: 1024px; font-size: 1.2em;">
  <tr>
    <td align="left">
      You are: <b>${c.user.username}</b>
    </td>
    <td align="right">
      %if c.user.anonymous:
        <a href="${h.url_for('login')}">Login</a>
      %endif
    </td>
  </tr>
</table>


<table style="width: 1024px;" cellspacing="0" cellpadding="0">
  %if c.err:
    <tr>
      <td style="font-size: 1.4em;" colspan="8">
        <div class="error">${c.err_msg}</div>
      </td>
    </tr>
  %endif

  <tr class="top">
    <td style="font-size: 1.4em;" colspan="8">${"<b>/</b>".join(map( lambda i: h.link_to(i[0], h.url_for(path=i[1])), c.tree ))|n}</td>
  </tr>
  
  ${h.form(h.url_for(), method="POST")}
    %if len(c.dirs) == 0 and len(c.files) == 0:
      <tr class="notice">
        <td class="button">&nbsp;</td>
        <td colspan="7" class="left">Empty Directory</td>
      </tr>
    %else:
      %if len(c.dirs) == 0:
        <tr class="notice">
          <td class="button">&nbsp;</td>
          <td colspan="7" class="left">No Directories</td>
        </tr>
      %endif

      %for d in c.dirs:
        <tr class="dir">
          <td class="action">${h.checkbox( "paths", d.name )}</td>
          <td class="button">D</td>
          <td class="name" colspan="2">${h.link_to(d.name, url=h.url_for(path=d.url_path))}</td>
          <td class="size">0</td>
          <td class="mime">&nbsp;</td>
          <td class="owner">${d.owner}</td>
          <td class="mode">${d.mode_s}</td>
        </tr>
      %endfor
      
      %if len(c.files) == 0:
        <tr class="file">
          <td class="button">&nbsp;</td>
          <td class="left" colspan="7"><b>No Files</b></td>
        </tr>
      %endif
      
      %for f in c.files:
        <tr class="file">
          <td class="action" valign="middle">${h.checkbox( "paths", f.name )}</td>
          <td class="button">F</td>
          <td class="name">
            ${h.link_to(f.name, url=h.url_for(action="download", path=f.url_path))}
          </td>
          <td style="text-align: right; padding: 0 4px;">
            <b>${h.link_to( 'view', url=h.url_for(action="view", path=f.url_path) )}</b>
          </td>
          <td class="size">${h.fmt_size(f.size)|n}</td>
          <td class="mime">${f.mime}</td>
          <td class="owner">${f.owner}</td>
          <td class="mode">${f.mode_s}</td>
        </tr>
      %endfor
    %endif

    %if c.writable:
      <tr>
        <td colspan="8">
          <table style="width: 100%;" cellspacing="4" cellpadding="0">
            <tr>
              <td>
                ${h.submit('delete', 'Delete', 
                  onclick="return confirm('Are you sure wou want to delete the selected file(s)?')")}
              </td>
              <td style="width: 1%;">
                <table cellspacing="0" cellpadding="0">
                  <tr class="chmod-title">
                    <td></td>
                    <td align="center"><label for="ur">r</label></td>
                    <td align="center"><label for="uw">w</label></td>
                    <td align="center"><label for="ux">x</label></td>
                  </tr>
                  <tr class="chmod-opts">
                    <td class="chmod-desc">U:</td>
                    <td align="center">${h.checkbox('ur', id='ur', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('uw', id='uw', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('ux', id='ux', class_="chmod-checkbox")}</td>
                  </tr>
                </table>
              </td>
              <td style="width: 1%;">
                <table cellspacing="0" cellpadding="0">
                  <tr class="chmod-title">
                    <td></td>
                    <td align="center"><label for="gr">r</label></td>
                    <td align="center"><label for="gw">w</label></td>
                    <td align="center"><label for="gx">x</label></td>
                  </tr>
                  <tr class="chmod-opts">
                    <td class="chmod-desc">G:</td>
                    <td align="center">${h.checkbox('gr', id='gr', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('gw', id='gw', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('gx', id='gx', class_="chmod-checkbox")}</td>
                  </tr>
                </table>
              </td>
              <td style="width: 1%;">
                <table cellspacing="0" cellpadding="0">
                  <tr class="chmod-title">
                    <td></td>
                    <td align="center"><label for="or">r</label></td>
                    <td align="center"><label for="ow">w</label></td>
                    <td align="center"><label for="ox">x</label></td>
                  </tr>
                  <tr class="chmod-opts">
                    <td class="chmod-desc">O:</td>
                    <td align="center">${h.checkbox('or', id='or', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('ow', id='ow', class_="chmod-checkbox")}</td>
                    <td align="center">${h.checkbox('ox', id='ox', class_="chmod-checkbox")}</td>
                  </tr>
                </table>
              </td>
              <td style="width: 1%;">
                ${h.submit('chmod', 'Chmod', 
                  onclick="return confirm('Are you sure wou want to chmod the selected file(s)?')")}
              </td>
            </tr>
          </table>
        </td>
      </tr>
      ${h.end_form()}
      <tr>
        <td colspan="8">
          <table style="width: 100%;">
            <tr>
              <td>
                ${h.form(h.url_for(action='upload'), method="PUT", multipart=True)}
                  Upload file: ${h.file('file')} ${h.submit('upload', 'Upload')}
                ${h.end_form()}
              </td>
              <td>
                ${h.form(h.url_for(action='upload'), method="PUT", multipart=True)}
                  Create directory: ${h.text('dir')} ${h.submit('upload', 'Create')}
                ${h.end_form()}
              </td>
            </tr>
          </table>
        </td>
      </tr>
    %else:
      <tr>
        <td colspan="8" align="center" style="padding: 4px 0;"><b>Directory not writable by you</b></td>
      </tr>
      ${h.end_form()}
    %endif # writable
</table>
