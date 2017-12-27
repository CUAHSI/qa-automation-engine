/*     
 *    
 *  Author     : Neal DeBuhr
 *  Version    : DEVS-Suite 3.0.0  
 *  Date       : 12-27-2017
 */
package CoreOne;
import java.awt.*;

import GenCol.*;

import model.modeling.*;
import model.simulation.*;

import view.modeling.ViewableAtomic;
import view.modeling.ViewableComponent;
import view.modeling.ViewableDigraph;
import view.simView.*;

public class AutomatedTestingEngine extends ViewableDigraph {
    protected int number_nodes;
    protected int number_jobs;
    // protected Array executors;
    
    public AutomatedTestingEngine(){
	super("AutomatedTestingEngine");
	number_nodes = 3;
	number_jobs = 10;
	
	ViewableAtomic hub = new hub("hub", number_nodes, number_jobs);
	// Fix below later for extensibility
	ViewableAtomic executor0 = new executor("executor0", 1);
	ViewableAtomic executor1 = new executor("executor1", 1);
	ViewableAtomic executor2 = new executor("executor2", 1);
	
	add(hub);
	add(executor0);
	add(executor1);
	add(executor2);
	
	addCoupling(executor0, "out", hub, "status0");
	addCoupling(executor1, "out", hub, "status1");
	addCoupling(executor2, "out", hub, "status2");
	addCoupling(hub, "out0", executor0, "in");
	addCoupling(hub, "out1", executor1, "in");
	addCoupling(hub, "out2", executor2, "in");
    }
    
    /**
     * Automatically generated by the SimView program.
     * Do not edit this manually, as such changes will get overwritten.
     */
    public void layoutForSimView()
    {
        preferredSize = new Dimension(591, 269);
        ((ViewableComponent)withName("executor0")).setPreferredLocation(new Point(274, 216));
        ((ViewableComponent)withName("executor2")).setPreferredLocation(new Point(280, 152));
        ((ViewableComponent)withName("hub")).setPreferredLocation(new Point(57, 128));
        ((ViewableComponent)withName("executor1")).setPreferredLocation(new Point(285, 76));
    }
}
