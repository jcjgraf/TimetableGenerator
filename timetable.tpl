{# saved as cal.tpl #}
%See http://tex.stackexchange.com/q/268780/82389
\documentclass[crop, tikz]{standalone}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usetikzlibrary{shapes.multipart}

%Options for timetable contents
\def\firsthour{8}
\def\lasthour{17}
\def\daynames{Monday, Tuesday, Wednesday, Thursday, Friday}

%Options for timetable drawing
\def\daywidth{3.4cm}   %approx \textwidth / 6
\def\hourheight{2.2cm} %approx \textheight / (\lasthour - \firsthour + 1)

\begin{document}

\centering
\begin{tikzpicture}[
    x=\daywidth, y=-\hourheight,
    block/.style={
        draw, text width=\daywidth, minimum height=\hourheight, inner sep=0pt, align=flush center
    },
    hour/.style ={block, fill=yellow!40, font=\bfseries\Large,
        text width=0.6*\daywidth, xshift=0.2*\daywidth},
    day/.style  ={block, fill=yellow!40, font=\bfseries\Large,
        minimum height=0.5*\hourheight, yshift=-0.25*\hourheight},
    event details/.style={
        align=flush center,
        inner xsep=0pt, inner ysep=1pt,
        rectangle split, rectangle split parts=3,
        text width=0.95*\daywidth
    },
    name/.style ={font=\normalsize},
    desc/.style ={font=\small\itshape},
    loc/.style  ={font=\small},
    hours/.style={minimum height=#1*\hourheight}
]

{%- for name, color in names -%}
    \tikzset{ {{name}}/.style={block, fill={{color}}!20, draw={{color}}!50!black, thick} }
{% endfor %}

\draw[help lines, xshift=0.5*\daywidth, yshift=0.5*\hourheight]
    (0, \firsthour) grid [xstep=\daywidth, ystep=\hourheight] (5, \lasthour);

\pgfmathtruncatemacro\secondhour{\firsthour + 1}
\foreach \end[remember=\end as \start (initially \firsthour)] in {\secondhour, ..., \lasthour} {
    \node[hour] at (0, \start) {\start--\end};
}

\foreach \day[count=\daynum] in \daynames {
    \node[day] at (\daynum, \firsthour-1) {\day};
}

{%- for day in days -%}
    {%- set dayloop = loop -%}
    {%- for time, event in day.items() -%}
        {%- set y = time  + (event.duration - 1) / 2 -%}
    \node[{{event.title}}, hours={{event.duration}}] at ( {{ dayloop.index }} , {{ y }} ) {};

    \node[event details] at ( {{ dayloop.index }} , {{ y }} ) {
        \nodepart[name]{one}   \strut {{ event.title }} 
        \nodepart[desc]{two}   \strut {{ event.description }}
        \nodepart[loc] {three} \strut {{ event.location }}
    };
    {%- endfor %}
{% endfor %}

\end{tikzpicture}
\end{document}
