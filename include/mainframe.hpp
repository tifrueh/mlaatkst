#pragma once

#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif


class MainFrame : public wxFrame {
    public:
        MainFrame(wxString title);
        wxAboutDialogInfo GetInfo();

    private:
        wxAboutDialogInfo info;
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

        wxButton* buttonOK = nullptr;

        wxStaticText* result = nullptr;

        wxButton* buttonCopy = nullptr;
        wxButton* buttonReset = nullptr;

        void OnClose(wxCommandEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnRadioBox(wxCommandEvent& event);
        void showDialogue();
        void hideAllInputs();
        void showInputGroupZero();
        void showInputGroupOne();
        void showInputGroupTwo();
};
