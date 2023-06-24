// MLAatKST: Footnote helper for KST students
// Copyright (C) 2023 Timo Früh
// The full copyright notice can be found at the start of ../src/main.cpp

#pragma once

#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

namespace qft {

    wxString bookFirstQuotation(const wxString& authorName,
                                const wxString& title,
                                const wxString& subtitle,
                                const wxString& edition,
                                const wxString& publisher,
                                const wxString& location,
                                const wxString& year,
                                const wxString& pageS );

    wxString bookSecondQuotation(const wxString& authorLastName,
                                 const wxString& year,
                                 const wxString& pageS);

    wxString web(const wxString& authorName,
                 const wxString& title,
                 const wxString& subtitle,
                 const wxString& url,
                 const wxString& date);
};
