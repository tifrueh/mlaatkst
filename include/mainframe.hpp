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
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void showDialogue();
};
