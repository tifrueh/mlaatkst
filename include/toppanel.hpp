// MLAatKST: Footnote helper for KST students
// Copyright (C) 2023 Timo Früh
// The full copyright notice can be found at the start of ../src/main.cpp

#pragma once

#include <wx/wxprec.h>
#include <wx/generic/statbmpg.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

class TopPanel : public wxPanel {
    public:
        TopPanel(wxWindow* parent);

        void processRadioBox();
        void processOK();
        void processCopy();

        void hideAllInputs();
        void showInputGroupZero();
        void showInputGroupOne();
        void showInputGroupTwo();
        void getInputGroupZero();
        void getInputGroupOne();
        void getInputGroupTwo();
        void clearAllInputs();

        void selectInputGroupZero();
        void selectInputGroupOne();
        void selectInputGroupTwo();

    private:
        wxGenericStaticBitmap* bar = nullptr;
        wxStaticText* appTitle = nullptr;
        wxRadioBox* radioBox = nullptr;
        wxBoxSizer* topsizer = nullptr;
        wxFlexGridSizer* inputSizer = nullptr;
        wxBoxSizer* buttonSizer = nullptr;

        wxStaticText* authorName = nullptr;
        wxStaticText* authorLastName = nullptr;
        wxStaticText* title = nullptr;
        wxStaticText* subtitle = nullptr;
        wxStaticText* edition = nullptr;
        wxStaticText* publisher = nullptr;
        wxStaticText* location = nullptr;
        wxStaticText* year = nullptr;
        wxStaticText* pageS = nullptr;
        wxStaticText* url = nullptr;
        wxStaticText* date = nullptr;

        wxTextCtrl* authorNameCtrl = nullptr;
        wxTextCtrl* authorLastNameCtrl = nullptr;
        wxTextCtrl* titleCtrl = nullptr;
        wxTextCtrl* subtitleCtrl = nullptr;
        wxTextCtrl* editionCtrl = nullptr;
        wxTextCtrl* publisherCtrl = nullptr;
        wxTextCtrl* locationCtrl = nullptr;
        wxTextCtrl* yearCtrl = nullptr;
        wxTextCtrl* pageSCtrl = nullptr;
        wxTextCtrl* urlCtrl = nullptr;
        wxTextCtrl* dateCtrl = nullptr;

        wxString authorNameS;
        wxString authorLastNameS;
        wxString titleS;
        wxString subtitleS;
        wxString editionS;
        wxString publisherS;
        wxString locationS;
        wxString yearS;
        wxString pageSS;
        wxString urlS;
        wxString dateS;

        wxButton* buttonOK = nullptr;

        wxString resultS;
        wxStaticText* result = nullptr;

        wxButton* buttonCopy = nullptr;
        wxButton* buttonReset = nullptr;
};
