<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="xml" indent="yes"/>

    <!-- Template to exclude Hardware node -->
    <xsl:template match="Hardware" />

    <!-- Template for Blueprint -->
    <xsl:template match="/Blueprint">
        <Batch>
            <xsl:apply-templates/>
        </Batch>
    </xsl:template>

    <!-- Template to copy all content without change -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Template for HeatChill -->
    <xsl:template match="HeatChill">
        <Heating>
            <xsl:apply-templates select="@*|node()"/>
        </Heating>
    </xsl:template>

    <!-- Template for Procedure -->
    <xsl:template match="Procedure">
        <Sequence>
            <xsl:apply-templates/>
        </Sequence>
    </xsl:template>

    <!-- Template for Reagents -->
    <xsl:template match="Reagents">
        <AddOnce>
            <xsl:apply-templates/>
        </AddOnce>
    </xsl:template>

</xsl:stylesheet>
