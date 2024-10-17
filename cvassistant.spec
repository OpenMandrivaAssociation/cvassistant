%define debug_package   %{nil}
%define oname CVAssistant

#define distsuffix mrb

Name:		cvassistant
Summary:	Create resumes in Word.docx format
Version:	2.0.0
Release:	1
Group:		Education
License:	GPLv3
URL:		https://sourceforge.net/projects/%{name}
Source0:	http://heanet.dl.sourceforge.net/project/%{name}/%{name}_%{version}.tar.bz2

BuildRequires:	qt5-devel
BuildRequires:	qmake5
BuildRequires:	desktop-file-utils
BuildRequires:	txt2man
BuildRequires:	gzip

%description
CV Assistant helps you create specialized 
resumes in Word .docx format fast and easy. 
The idea is to have a master resume with all 
skills and experiences in it. 
Then based on skills mentioned 
in the job advertisement, export a 
clean but well formatted word .docx file as a 
summarized resume with only relevant skills in it.
This increases your chance of getting a job 
interview as most companies are using 
Applicant Tracking Software (ATS) or at 
best hiring managers which may be unaware 
of similarity between phrases like skilled 
in MS Word, familiar with 
Microsoft Word and Fully experienced with office suites.
So job seekers need to create 
specialized resumes for each and every 
job position with the same wordings used 
in the advertisement. Add all your skills 
to CV Assistant, pick only relevant ones.
It also creates cover letters! 
Again, write all possible sentences, 
and select those relevant ones per job post.

%prep
%setup -qn %{oname}
chmod 644 README licence.txt
txt2man README > cvassistant.1
gzip cvassistant.1
chmod 644 templates/*

%build
%qmake_qt5  
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/templates
cp -R templates/* %{buildroot}%{_datadir}/%{name}/templates

mkdir -p %{buildroot}%{_mandir}/man1
cp cvassistant.1.gz  %{buildroot}%{_mandir}/man1/

%files 
%doc README licence.txt
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/
%{_datadir}/%{name}/templates
%{_mandir}/man1/%{name}*.1.*


