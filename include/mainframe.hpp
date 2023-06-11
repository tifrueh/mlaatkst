#pragma once

#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "toppanel.hpp"

class MainFrame : public wxFrame {
    public:
        MainFrame(wxString title);
        wxAboutDialogInfo GetInfo();

    private:
        wxAboutDialogInfo info;
        wxMenu* menuFile = nullptr;
        wxMenu* menuEdit = nullptr;
        wxMenu* menuHelp = nullptr;
        wxMenuBar* menuBar = nullptr;
        TopPanel* topPanel = nullptr;
        wxBoxSizer* topPanelSizer = nullptr;
        void OnClose(wxCommandEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        void OnRadioBox(wxCommandEvent& event);
        void OnOK(wxCommandEvent& event);
        void OnClear(wxCommandEvent& event);
        void OnCopy(wxCommandEvent& event);
        void OnOne(wxCommandEvent& event);
        void OnTwo(wxCommandEvent& event);
        void OnThree(wxCommandEvent& event);
        void OnGitHub(wxCommandEvent& event);
};
