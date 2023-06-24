// MLAatKST: Footnote helper for KST students
// Copyright (C) 2023 Timo Früh
// The full copyright notice can be found at the start of main.cpp

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
            result = authorName + wxT(", ") + title + wxT(", ") + edition + wxT(". ") + _("edition") + wxT(", ")
                         + publisher + wxT(", ") + year + wxT(", ") + _("p") + wxT(". ") + pageS + wxT(".");
        } else {
            result = authorName + wxT(", ") + title + wxT(", ") + subtitle + wxT(", ") + edition + wxT(". ") + _("edition") + wxT(", ")
                         + publisher + wxT(", ") + year + wxT(", ") + _("p") + wxT(". ") + pageS + wxT(".");
        }

        return result;
}

wxString qft::bookSecondQuotation(const wxString& authorLastName,
                                 const wxString& year,
                                 const wxString& pageS) {
        wxString result = authorLastName + wxT(", ") + year + wxT(", ") + _("p") + wxT(". ") + pageS + wxT(".");
        return result;
}

wxString qft::web(const wxString& authorName,
                 const wxString& title,
                 const wxString& subtitle,
                 const wxString& url,
                 const wxString& date) {
        wxString result;

        if (subtitle.Strip() == wxT("")) {
                result = authorName + wxT(", ") + title + wxT(", ") + url + wxT(", ") + date + wxT(".");
            } else {
                result = authorName + wxT(", ") + title + wxT(", ") + wxT(", ") + subtitle + wxT(", ") + url + wxT(", ") + date + wxT(".");
        }

        return result;
    }
