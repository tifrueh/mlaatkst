#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "quotation_formatter.hpp"

wxString qft::bookFirstQuotation(const wxString& authorName,
                                const wxString& title,
                                const wxString& subtitle,
                                const wxString& edition,
                                const wxString& publisher,
                                const wxString& location,
                                const wxString& year,
                                const wxString& pageS ) {
        wxString result;

        if (subtitle.Strip() == wxT("")) {
            result = authorName + _(", ") + title + _(", ") + edition + _(". edition, ")
                         + publisher + _(", ") + year + _(", p. ") + pageS + _(".");
        } else {
            result = authorName + _(", ") + title + _(", ") + subtitle + _(", ") + edition + _(". edition, ")
                         + publisher + _(", ") + year + _(", p. ") + pageS + _(".");
        }

        return result;
}

wxString qft::bookSecondQuotation(const wxString& authorLastName,
                                 const wxString& year,
                                 const wxString& pageS) {
        wxString result = authorLastName + _(", ") + year + _(", p. ") + pageS + _(".");
        return result;
}

wxString qft::web(const wxString& authorName,
                 const wxString& title,
                 const wxString& subtitle,
                 const wxString& url,
                 const wxString& date) {
        wxString result;

        if (subtitle.Strip() == wxT("")) {
                result = authorName + _(", ") + title + _(", ") + url + _(", ") + date + _(".");
            } else {
                result = authorName + _(", ") + title + _(", ") + _(", ") + subtitle + _(", ") + url + _(", ") + date + _(".");
        }

        return result;
    }
