import React from "react";
import "./skills.css";
import Frontend from "./Frontend";
import Backend from "./Backend";

const Skills = () => {
    return (
        <section className="skills section" id="skills">
            <h2 className="section__title">Skills</h2>
            <span className="section__subtitle">Here are some of the concepts, languages & frameworks that I am familiar with 📖🖋️</span>

            <div className="skills__container container grid">
                <Frontend />
                <Backend />
            </div>
        </section>
    );
};

export default Skills