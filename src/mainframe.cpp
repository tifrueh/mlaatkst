// MLAatKST: Footnote helper for KST students
// Copyright (C) 2023 Timo Früh
// The full copyright notice can be found at the start of main.cpp

#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>
#include <wx/clipbrd.h>

#include "id.hpp"
#include "mainframe.hpp"
#include "quotation_formatter.hpp"
#include "toppanel.hpp"


MainFrame::MainFrame(wxString title) : wxFrame(NULL, wxID_ANY, title) {

    info.SetName(wxT("MLAatKST"));
    info.SetVersion(wxT("2.0.0"));
    info.SetCopyright(wxT(
        "Copyright (C) 2022-2023 Timo Früh\n"
        "This program is free and open source software, licensed under the GNU General Public License 3.0. "
        "For futher information, see <https://www.gnu.org/licenses/>."
    ));

    menuFile = new wxMenu;
    menuFile->Append(wxID_EXIT, _("Quit MLAatKST") + wxT("\tCtrl-q"));
    menuFile->Append(wxID_CLOSE, _("Close Window") + wxT("\tCtrl-w"));

    menuEdit = new wxMenu;
    menuEdit->Append(winID::ID_OK_MENU, wxT("&") + _("Process inputs") + wxT("\tCtrl-Enter"));
    menuEdit->Append(winID::ID_COPY_MENU, wxT("&") + _("Copy footnote") + wxT("\tCtrl-Shift-c"));
    menuEdit->AppendSeparator();
    menuEdit->Append(winID::ID_ONE, wxT("&") + _("First mention of a book") + wxT("\tCtrl-1"));
    menuEdit->Append(winID::ID_TWO, wxT("&") + _("Second mention of a book") + wxT("\tCtrl-2"));
    menuEdit->Append(winID::ID_THREE, wxT("&") + _("Mention of a website") + wxT("\tCtrl-3"));
    menuEdit->AppendSeparator();
    menuEdit->Append(winID::ID_CLEAR_MENU, wxT("&") + _("Clear inputs") + wxT("\tCtrl-0"));
 
    menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT, wxT("&") + _("About MLAatKST") + wxT("\tCtrl-?"));
    menuHelp->Append(winID::ID_GITHUB, wxT("&") + _("MLAatKST on GitHub"));
 
    menuBar = new wxMenuBar;
    menuBar->Append(menuFile, wxT("&") + _("File"));
    menuBar->Append(menuEdit, wxT("&") + _("Edit"));
    menuBar->Append(menuHelp, wxT("&") + _("Help"));

    this->SetMenuBar(menuBar);

    Bind(wxEVT_MENU, &MainFrame::OnQuit, this, wxID_EXIT);
    Bind(wxEVT_MENU, &MainFrame::OnClose, this, wxID_CLOSE);
    Bind(wxEVT_MENU, &MainFrame::OnAbout, this, wxID_ABOUT);
    Bind(wxEVT_MENU, &MainFrame::OnCopy, this, winID::ID_COPY_MENU);
    Bind(wxEVT_MENU, &MainFrame::OnClear, this, winID::ID_CLEAR_MENU);
    Bind(wxEVT_MENU, &MainFrame::OnOK, this, winID::ID_OK_MENU);
    Bind(wxEVT_MENU, &MainFrame::OnGitHub, this, winID::ID_GITHUB);
    Bind(wxEVT_MENU, &MainFrame::OnOne, this, winID::ID_ONE);
    Bind(wxEVT_MENU, &MainFrame::OnTwo, this, winID::ID_TWO);
    Bind(wxEVT_MENU, &MainFrame::OnThree, this, winID::ID_THREE);
    Bind(wxEVT_RADIOBOX, &MainFrame::OnRadioBox, this, winID::ID_RADIOBOX);
    Bind(wxEVT_BUTTON, &MainFrame::OnOK, this, wxID_OK);
    Bind(wxEVT_BUTTON, &MainFrame::OnClear, this, winID::ID_CLEAR);
    Bind(wxEVT_BUTTON, &MainFrame::OnCopy, this, winID::ID_COPY);

    topPanel = new TopPanel(this);

    topPanelSizer = new wxBoxSizer(wxVERTICAL);
    topPanelSizer->Add(
        topPanel,
        1,
        wxEXPAND,
        0
    );

    SetSizerAndFit(topPanelSizer);
}

wxAboutDialogInfo MainFrame::GetInfo() {
    return info;
}

void MainFrame::OnClose(wxCommandEvent& event) {
    Close();
}

void MainFrame::OnAbout(wxCommandEvent& event) {
    wxAboutBox(GetInfo(), this);
}

void MainFrame::OnQuit(wxCommandEvent& event) {
    Close();
}

void MainFrame::OnClear(wxCommandEvent& event) {
    topPanel->clearAllInputs();
}

void MainFrame::OnRadioBox(wxCommandEvent& event) {
    topPanel->processRadioBox();
}

void MainFrame::OnOK(wxCommandEvent& event) {
    topPanel->processOK();
}

void MainFrame::OnCopy(wxCommandEvent& event) {
    topPanel->processCopy();
}

void MainFrame::OnGitHub(wxCommandEvent& event) {
    wxLaunchDefaultBrowser(wxT("https://github.com/tifrueh/mlaatkst"));
}

void MainFrame::OnOne(wxCommandEvent& event) {
    topPanel->selectInputGroupZero();
}

void MainFrame::OnTwo(wxCommandEvent& event) {
    topPanel->selectInputGroupOne();
}

void MainFrame::OnThree(wxCommandEvent& event) {
    topPanel->selectInputGroupTwo();
}
