#include <wx/wxprec.h>
 
#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/aboutdlg.h>

#include "id.hpp"
#include "mainframe.hpp"


MainFrame::MainFrame(wxString title) : wxFrame(NULL, wxID_ANY, title) {

    info.SetName(wxT("MLAatKST"));
    info.SetVersion(wxT("2.0.0-dev"));
    info.SetCopyright(wxT(
        "Copyright (C) 2022-2023 Timo Früh\n"
        "This program is free and open source software, licensed under the GNU General Public License 3.0. "
        "For futher information, see <https://www.gnu.org/licenses/>."
    ));

    wxMenu *menuFile = new wxMenu;
    menuFile->Append(wxID_EXIT, wxT("&Quit MLAatKST\tCtrl-q"));
    menuFile->Append(wxID_CLOSE, wxT("&Close Window\tCtrl-w"));
 
    wxMenu *menuHelp = new wxMenu;
    menuHelp->Append(wxID_ABOUT, wxT("&About MLAatKST\tCtrl-?"));
 
    wxMenuBar *menuBar = new wxMenuBar;
    menuBar->Append(menuFile, "&File");
    menuBar->Append(menuHelp, "&Help");

    this->SetMenuBar(menuBar);

    Bind(wxEVT_MENU, &MainFrame::OnQuit, this, wxID_EXIT);
    Bind(wxEVT_MENU, &MainFrame::OnClose, this, wxID_CLOSE);
    Bind(wxEVT_MENU, &MainFrame::OnAbout, this, wxID_ABOUT);

    showDialogue();
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

void MainFrame::showDialogue() {
    wxStaticText* appTitle = new wxStaticText(this, wxID_ANY, wxT("MLA Standart an der KST"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL);
    wxFont titleFont = appTitle->GetFont();
    titleFont.Scale(2);
    titleFont.MakeBold();
    appTitle->SetFont(titleFont);

    wxArrayString radioBoxOptions;
    radioBoxOptions.Add(wxT("&Erstnennung Buch"));
    radioBoxOptions.Add(wxT("&Zweitnennung Buch"));
    radioBoxOptions.Add(wxT("&Webzitat"));
    wxRadioBox* radioBox = new wxRadioBox(this, winID::ID_RADIOBOX, wxT("Optionen"), wxDefaultPosition, wxDefaultSize, radioBoxOptions, 3, wxRA_SPECIFY_COLS);

    wxStaticText* authorName = new wxStaticText(this, wxID_ANY, wxT("Name des Autors / der Autorin: (Nachname, Vorname)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* title = new wxStaticText(this, wxID_ANY, wxT("Titel des Werks"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* subtitle = new wxStaticText(this, wxID_ANY, wxT("Untertitel: (leer lassen wenn nicht vorhanden)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* edition = new wxStaticText(this, wxID_ANY, wxT("Auflage: (Zahl eingeben)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* publisher = new wxStaticText(this, wxID_ANY, wxT("Verlag"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* location = new wxStaticText(this, wxID_ANY, wxT("Ort"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* year = new wxStaticText(this, wxID_ANY, wxT("Jahr"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* pageS = new wxStaticText(this, wxID_ANY, wxT("Zitierte Seite(n):"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* url = new wxStaticText(this, wxID_ANY, wxT("URL:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);
    wxStaticText* date = new wxStaticText(this, wxID_ANY, wxT("Herunterladedatum:"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_VERTICAL);



    wxTextCtrl* authorNameCtrl = new wxTextCtrl(this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize(250, wxDefaultSize.GetY()));
    wxTextCtrl* titleCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* subtitleCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* editionCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* publisherCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* locationCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* yearCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* pageSCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* urlCtrl = new wxTextCtrl(this, wxID_ANY);
    wxTextCtrl* dateCtrl = new wxTextCtrl(this, wxID_ANY);

    wxFlexGridSizer* inputSizer = new wxFlexGridSizer(2, 0, 20);
    inputSizer->AddGrowableCol(1);
    inputSizer->Add(authorName, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(authorNameCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(title, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(titleCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(subtitle, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(subtitleCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(edition, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(editionCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(publisher, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(publisherCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(location, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(locationCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(year, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(yearCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(pageS, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(pageSCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(url, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(urlCtrl, 0, wxEXPAND | wxALL, 5);
    inputSizer->Add(date, 0, wxALIGN_CENTER_VERTICAL | wxALIGN_LEFT | wxALL, 5);
    inputSizer->Add(dateCtrl, 0, wxEXPAND | wxALL, 5);

    wxBoxSizer* topsizer = new wxBoxSizer(wxVERTICAL);

    topsizer->Add(
        appTitle,
        0,
        wxEXPAND |
        wxALL,
        10
    );

    topsizer->Add(
        radioBox,
        0,
        wxALIGN_CENTRE |
        wxBOTTOM | wxLEFT | wxRIGHT,
        10
    );

    topsizer->Add(
        inputSizer,
        1,
        wxEXPAND |
        wxALL,
        10
    );

    SetSizerAndFit(topsizer);
}
