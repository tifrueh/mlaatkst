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
            result = wxT("" + authorName + ", " + title + ", " + edition + ". edition, "
                         + publisher + ", " + year + ", p. " + pageS + ".");
        } else {
            result = wxT("" + authorName + ", " + title + ", " + subtitle + ", " + edition + ". edition, "
                         + publisher + ", " + year + ", p. " + pageS + ".");
        }

        return result;
}

wxString qft::bookSecondQuotation(const wxString& authorLastName,
                                 const wxString& year,
                                 const wxString& pageS) {
        wxString result = wxT("" + authorLastName + ", " + year + ", p. " + pageS + ".");
        return result;
}

wxString qft::web(const wxString& authorName,
                 const wxString& title,
                 const wxString& subtitle,
                 const wxString& url,
                 const wxString& date) {
        wxString result;

        if (subtitle.Strip() == wxT("")) {
                result = wxT("" + authorName + ", " + title + ", " + url + ", " + date + ".");
            } else {
                result = wxT("" + authorName + ", " + title + ", " + ", " + subtitle + ", " + url + ", " + date + ".");
        }

        return result;
    }
